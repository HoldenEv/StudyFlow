import re
from tkinter import messagebox
from chat import ask_chat_gpt

def execute_command(event, command_entry, text_area):
    """Processes and executes commands entered in the command line."""
    command = command_entry.get().strip().lower()

    if command == "search":
        content = text_area.get(1.0, "end")

        # Search for questions in the format ~(sample question)~
        match = re.search(r"~\((.*?)\)~", content)
        if match:
            question = match.group(1)
            ask_chat_gpt(question)  # Call ChatGPT script

    elif command == "clear":
        text_area.delete(1.0, "end")
        messagebox.showinfo("Command Executed", "Text cleared!")

    elif command == "exit":
        text_area.quit()

    else:
        messagebox.showerror("Invalid Command", f"Unknown command: {command}")

    command_entry.delete(0, "end")  # Clear command entry after execution
