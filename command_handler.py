import re
import json
from tkinter import messagebox
from chat import ask_chat_gpt

QA_STORAGE_FILE = "qa_storage.json"

def load_stored_answers():
    """Loads stored Q&A pairs from the JSON file."""
    try:
        with open(QA_STORAGE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_stored_answers(data):
    """Saves Q&A pairs to the JSON file."""
    with open(QA_STORAGE_FILE, "w") as file:
        json.dump(data, file, indent=4)

def execute_command(event, command_entry, text_area, response_box):
    """Processes and executes commands entered in the command line."""
    command = command_entry.get().strip().lower()
    
    if command == "search":
        content = text_area.get(1.0, "end")
        matches = re.findall(r"~\((.*?)\)~", content)  # Find all questions

        if not matches:
            messagebox.showinfo("Search", "No questions found in the text.")
            return

        stored_answers = load_stored_answers()
        response_box.config(state="normal")
        response_box.delete("1.0", "end")

        for question in matches:
            if question in stored_answers:
                response = stored_answers[question]
            else:
                response = ask_chat_gpt(question, response_box)
                stored_answers[question] = response  # Save new answer

            # Display each question-answer pair
            response_box.insert("end", f"Q: {question}\nA: {response}\n\n")

        response_box.config(state="disabled")
        save_stored_answers(stored_answers)  # Save updated data

    elif command == "clear":
        text_area.delete(1.0, "end")
        messagebox.showinfo("Command Executed", "Text cleared!")

    elif command == "help":
        print("Still working on this")
        pass

    elif command == "exit":
        text_area.quit()

    else:
        messagebox.showerror("Invalid Command", f"Unknown command: {command}")

    command_entry.delete(0, "end")  # Clear command input
