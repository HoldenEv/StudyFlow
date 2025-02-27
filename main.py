import tkinter as tk
from text_editor import create_text_area
from file_operations import new_file, open_file, save_file
from font_manager import change_font, increase_font_size, decrease_font_size
# from key_handler import handle_key
from command_handler import execute_command

# Create main window
root = tk.Tk()
root.title("StudyFlow")

# Create text area
text_area, current_font = create_text_area(root)

# Bind key combinations to font size adjustment
root.bind("<Command-=>", lambda event: increase_font_size(current_font))
root.bind("<Command-minus>", lambda event: decrease_font_size(current_font))
root.bind("<Control-=>", lambda event: increase_font_size(current_font))
root.bind("<Control-minus>", lambda event: decrease_font_size(current_font))

# Create menu bar
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

# Bind all key presses to handle_key function
#text_area.bind("<KeyPress>", lambda event: handle_key(event, text_area))

# Command line input at the bottom
command_entry = tk.Entry(root)
command_entry.pack(fill=tk.X, padx=5, pady=5)

# Bind the Enter key to execute commands
command_entry.bind("<Return>", lambda event: execute_command(event, command_entry, text_area))

# Run the application
root.mainloop()
