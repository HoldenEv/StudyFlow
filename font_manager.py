import tkinter.simpledialog
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox

def change_font(current_font):
    """Display a font selection window and apply the chosen font."""
    font_families = sorted(tkFont.families())  # Get available fonts
    
    # Create the font selection window
    font_window = tk.Toplevel()
    font_window.title("Select Font")
    font_window.geometry("300x400")  # Set window size
    
    # Create a scrollbar for the font list
    scrollbar = tk.Scrollbar(font_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Create a listbox with available fonts
    font_listbox = tk.Listbox(font_window, yscrollcommand=scrollbar.set, selectmode=tk.SINGLE)
    
    # Insert all fonts into the listbox
    for font in font_families:
        font_listbox.insert(tk.END, font)
    
    font_listbox.pack(fill=tk.BOTH, expand=True)
    scrollbar.config(command=font_listbox.yview)  # Attach scrollbar to listbox

    def apply_font():
        """Apply the selected font."""
        selected_font_index = font_listbox.curselection()
        if selected_font_index:
            selected_font = font_listbox.get(selected_font_index)
            current_font.configure(family=selected_font)
        else:
            messagebox.showerror("No Font Selected", "Please select a font before applying.")

        font_window.destroy()  # Close the selection window

    # Button to apply selected font
    apply_button = tk.Button(font_window, text="Apply", command=apply_font)
    apply_button.pack(pady=5)

    font_window.mainloop()


def increase_font_size(current_font):
    """Increase the font size."""
    current_size = current_font.cget("size")
    current_font.configure(size=current_size + 2)

def decrease_font_size(current_font):
    """Decrease the font size."""
    current_size = current_font.cget("size")
    if current_size > 8:
        current_font.configure(size=current_size - 2)
