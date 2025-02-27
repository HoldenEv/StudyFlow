import tkinter.simpledialog
import tkinter.font as tkFont
from tkinter import messagebox

def change_font(current_font):
    """Change the font family of the text area."""
    font_families = sorted(tkFont.families())

    font_choice = tkinter.simpledialog.askstring(
        "Select Font", 
        f"Available fonts:\n{', '.join(font_families)}\n\nEnter a font name:"
    )

    if font_choice in font_families:
        current_font.configure(family=font_choice)
    else:
        messagebox.showerror("Invalid Font", "The selected font is not available.")

def increase_font_size(current_font):
    """Increase the font size."""
    current_size = current_font.cget("size")
    current_font.configure(size=current_size + 2)

def decrease_font_size(current_font):
    """Decrease the font size."""
    current_size = current_font.cget("size")
    if current_size > 8:
        current_font.configure(size=current_size - 2)
