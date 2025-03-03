from openai import OpenAI
from tkinter import messagebox
import os
import tkinter as tk

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

        # Return response for storage
        return response

    except Exception as e:
        messagebox.showerror("Error", f"Failed to get response from ChatGPT: {str(e)}")
        return "Error retrieving response."