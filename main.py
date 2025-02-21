import tkinter as tk
from tkinter import filedialog, messagebox
import tkinter.font as tkFont
import tkinter.simpledialog
import time
import re
from chat import * 

# Create main window
root = tk.Tk()
root.title("StudyFlow")

# Create text area
text_area = tk.Text(root, wrap="word", undo=True)
text_area.pack(expand=True, fill=tk.BOTH)

# Variables to track key sequence
key_sequence = []
last_key_time = 0
sequence_timeout = 0.5  # Max time (in seconds) between key presses

# Track the font size
current_font = tkFont.Font(family="Apple Braille", size=12)
text_area.configure(font=current_font)

def change_font():
    """Change the font family of the text area."""
    # List of available font families in tkinter
    font_families = sorted(tkFont.families())

    # Open a dialog to select a font
    font_choice = tkinter.simpledialog.askstring(
        "Select Font", 
        f"Available fonts:\n{', '.join(font_families)}\n\nEnter a font name:",
        parent=root
    )

    if font_choice in font_families:
        # Change the font of the text area
        current_font.configure(family=font_choice)
    else:
        messagebox.showerror("Invalid Font", "The selected font is not available.")

def increase_font_size():
    """Increase the font size of the text area."""
    current_size = current_font.cget("size")
    current_font.configure(size=current_size + 2)

def decrease_font_size():
    """Decrease the font size of the text area."""
    current_size = current_font.cget("size")
    if current_size > 8:  # Prevent font from becoming too small
        current_font.configure(size=current_size - 2)

# Bind key combinations to font size adjustment
root.bind("<Command-=>", lambda event: increase_font_size())  # Command and + on macOS
root.bind("<Command-minus>", lambda event: decrease_font_size())  # Command and - on macOS
root.bind("<Control-=>", lambda event: increase_font_size())  # Ctrl and + on Windows
root.bind("<Control-minus>", lambda event: decrease_font_size())  # Ctrl and - on Windows

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                content = file.read()
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {str(e)}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                content = text_area.get(1.0, tk.END)
                file.write(content.strip())  # Remove trailing newline
                messagebox.showinfo("Success", "File saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {str(e)}")

def print_current_contents():
    content = text_area.get(1.0, tk.END).strip()  # Get all text from the text area, remove trailing newline
    print(content)

def handle_key(event):
    global key_sequence, last_key_time

    current_time = time.time()
    # If too much time has passed, reset the sequence
    if current_time - last_key_time > sequence_timeout:
        key_sequence = []

    # Add the current key to the sequence
    key_sequence.append(event.char)

    # Check for the "po" sequence
    if "".join(key_sequence[-2:]) == "po":
        content = text_area.get(1.0, tk.END)

        # Search for questions in the format ~(sample question)~
        match = re.search(r"~\((.*?)\)~", content)
        if match:
            question = match.group(1)
            ask_chat_gpt(question)  # Ask ChatGPT the detected question

        key_sequence = []  # Reset sequence

    last_key_time = current_time

# Create menu bar
menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Fonts", command=change_font)

file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add menu to the window
root.config(menu=menu_bar)

# Bind all key presses to handle_key function
text_area.bind("<KeyPress>", handle_key)

# Run the application
root.mainloop()