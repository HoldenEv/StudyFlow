import tkinter as tk
from text_editor import create_text_area
from file_operations import new_file, open_file, save_file
from font_manager import change_font, increase_font_size, decrease_font_size
# from key_handler import handle_key
from command_handler import execute_command

# Create main window
root = tk.Tk()
root.title("StudyFlow")
root.geometry("1000x600")  # Set initial size for better layout

# === Create Sidebar for ChatGPT Response ===
chat_frame = tk.Frame(root, width=250, bg="#000000")
chat_frame.pack(side=tk.LEFT, fill=tk.Y)

chat_label = tk.Label(chat_frame, text="ChatGPT Response", font=("Arial", 12, "bold"), fg="white", bg="#000000")
chat_label.pack(pady=5)

response_box = tk.Text(chat_frame, wrap=tk.WORD, state=tk.DISABLED, width=30, height=50, bg="#1e1e1e", fg="white")
response_box.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# === Create a Frame to Hold Text Editor & Command Entry ===
main_frame = tk.Frame(root)
main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Create Text Area
text_area, current_font = create_text_area(main_frame)

# Command line input at the bottom
command_entry = tk.Entry(main_frame)
command_entry.pack(fill=tk.X, padx=5, pady=5)

# === Menu Bar ===
menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=lambda: new_file(text_area))
file_menu.add_command(label="Open", command=lambda: open_file(text_area))
file_menu.add_command(label="Save", command=lambda: save_file(text_area))
file_menu.add_command(label="Fonts", command=lambda: change_font(current_font))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add menu to the window
root.config(menu=menu_bar)

# === Bindings ===
root.bind("<Command-=>", lambda event: increase_font_size(current_font))
root.bind("<Command-minus>", lambda event: decrease_font_size(current_font))
root.bind("<Control-=>", lambda event: increase_font_size(current_font))
root.bind("<Control-minus>", lambda event: decrease_font_size(current_font))

# Bind Enter key in command input to execute commands
command_entry.bind("<Return>", lambda event: execute_command(event, command_entry, text_area, response_box))

# Run the application
root.mainloop()
