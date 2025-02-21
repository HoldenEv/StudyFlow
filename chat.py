from openai import OpenAI
from tkinter import messagebox
import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # grab api from file

def ask_chat_gpt(question):
    """Send the question to ChatGPT and print the response."""
    try:
        completion = client.chat.completions.create(model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": question
            }
        ])
        
        print("ChatGPT Response:", completion.choices[0].message.content)
        messagebox.showinfo("ChatGPT Response", completion.choices[0].message.content)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to get response from ChatGPT: {str(e)}")