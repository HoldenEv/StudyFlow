# from openai import OpenAI
# from tkinter import messagebox
# import os
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # grab api from file

# def ask_chat_gpt(question):
#     """Send the question to ChatGPT and print the response."""
#     try:
#         completion = client.chat.completions.create(model="gpt-4",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {
#                 "role": "user",
#                 "content": question
#             }
#         ])
        
#         print("ChatGPT Response:", completion.choices[0].message.content)
#         messagebox.showinfo("ChatGPT Response", completion.choices[0].message.content)
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to get response from ChatGPT: {str(e)}")

import tkinter as tk
from openai import OpenAI
from tkinter import messagebox
import os

# OpenAI API Client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_chat_gpt(question, response_box):
    """Send the question to ChatGPT and display the response in the sidebar."""
    try:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )
        
        response = completion.choices[0].message.content

        # Clear previous responses and insert new one
        response_box.config(state=tk.NORMAL)  # Enable editing
        response_box.delete("1.0", tk.END)  # Clear previous text
        response_box.insert(tk.END, response)  # Insert new response
        response_box.config(state=tk.DISABLED)  # Disable editing
        
    except Exception as e:
        messagebox.showerror("Error", f"Failed to get response from ChatGPT: {str(e)}")



# Create sidebar for ChatGPT response
# chat_frame = tk.Frame(root, width=250, bg="#000000")
# chat_frame.pack(side=tk.LEFT, fill=tk.Y)

# chat_label = tk.Label(chat_frame, text="ChatGPT Response", font=("Arial", 12, "bold"), bg="#f0f0f0")
# chat_label.pack(pady=5)

# response_box = tk.Text(chat_frame, wrap=tk.WORD, state=tk.DISABLED, width=30, height=25)
# response_box.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)


# Bind Enter key to send question to ChatGPT
#command_entry.bind("<Return>", lambda event: ask_chat_gpt(command_entry.get(), response_box))


