from tkinter import filedialog, messagebox

def new_file(text_area):
    """Clear the text area to create a new file."""
    text_area.delete(1.0, "end")

def open_file(text_area):
    """Open and read a file into the text area."""
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                content = file.read()
                text_area.delete(1.0, "end")
                text_area.insert("end", content)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {str(e)}")

def save_file(text_area):
    """Save the current text to a file."""
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                content = text_area.get(1.0, "end").strip()  # Remove trailing newline
                file.write(content)
                messagebox.showinfo("Success", "File saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {str(e)}")
