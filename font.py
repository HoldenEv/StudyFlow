from tkinter import messagebox
import tkinter
import tkinter.font as tkFont

def change_font(root, current_font):
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