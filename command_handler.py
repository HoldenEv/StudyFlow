import re
from tkinter import messagebox
from chat import ask_chat_gpt


def execute_command(event, command_entry, text_area, response_box):
    """Processes and executes commands entered in the command line."""
    command = command_entry.get().strip().lower()

    if command.casefold() == "search":
        content = text_area.get(1.0, "end")

        # Search for questions in the format ~(sample question)~
        match = re.search(r"~\((.*?)\)~", content)
        if match:
            question = match.group(1)
            ask_chat_gpt(question, response_box)  # Call ChatGPT script

    elif command.casefold() == "clear":
        text_area.delete(1.0, "end")
        messagebox.showinfo("Command Executed", "Text cleared!")

    elif command.casefold() == "help":
        print("still working on this")
        pass

    elif command.casefold() == "exit":
        text_area.quit()

    else:
        messagebox.showerror("Invalid Command", f"Unknown command: {command}")

    command_entry.delete(0, "end")  # Clear command entry after execution
