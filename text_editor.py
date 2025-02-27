import tkinter as tk
import tkinter.font as tkFont

def create_text_area(root):
    """Creates and returns a text area widget with a default font."""
    text_area = tk.Text(root, wrap="word", undo=True)
    text_area.pack(expand=True, fill=tk.BOTH)

    # Default font setup
    current_font = tkFont.Font(family="Apple Braille", size=12)
    text_area.configure(font=current_font)

    return text_area, current_font