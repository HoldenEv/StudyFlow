import time
import re
from chat import ask_chat_gpt  # Assuming `ask_chat_gpt` is defined in chat.py

key_sequence = []
last_key_time = 0
sequence_timeout = 0.5  # Max time (in seconds) between key presses

def handle_key(event, text_area):
    """Track key sequences and trigger AI queries if detected."""
    global key_sequence, last_key_time

    current_time = time.time()
    if current_time - last_key_time > sequence_timeout:
        key_sequence = []

    key_sequence.append(event.char)

    if "".join(key_sequence[-2:]) == "po":
        content = text_area.get(1.0, "end")

        # Search for questions in the format ~(sample question)~
        match = re.search(r"~\((.*?)\)~", content)
        if match:
            question = match.group(1)
            ask_chat_gpt(question)  # Ask ChatGPT the detected question

        key_sequence = []

    last_key_time = current_time
