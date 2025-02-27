from tkinter import filedialog

def new_file(text_area):
    """Clears the text area for a new file."""
    text_area.delete(1.0, "end")

def open_file(text_area):
    """Opens a file and loads its content into the text area."""
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, "end")
            text_area.insert("end", file.read())

def save_file(text_area):
    """Saves the current content of the text area to a file."""
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, "end"))
