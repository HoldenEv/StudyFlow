import tkinter as tk
from tkinter import filedialog, messagebox
import time
import re
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # grab api from file

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

def ask_chat_gpt(question):
    """Send the question to ChatGPT and print the response."""
    try:
        completion = client.chat.completions.create(model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": question
            }
        ])
        
        print("ChatGPT Response:", completion.choices[0].message.content)
        messagebox.showinfo("ChatGPT Response", completion.choices[0].message.content)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to get response from ChatGPT: {str(e)}")

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
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add menu to the window
root.config(menu=menu_bar)

# Bind all key presses to handle_key function
text_area.bind("<KeyPress>", handle_key)

# Run the application
root.mainloop()