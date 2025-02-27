import tkinter as tk

def create_text_area(root):
    """Create and return a text area widget."""
    text_area = tk.Text(root, wrap="word", undo=True)
    text_area.pack(expand=True, fill=tk.BOTH)
    return text_area