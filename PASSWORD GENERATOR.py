import tkinter as tk
from tkinter import Label, Entry, Button
import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def generate_password_gui():
    def generate():
        try:
           
            length = int(length_entry.get())

          
            if length <= 0:
                result_label.config(text="Password length must be greater than 0.")
                return

     
            password = generate_password(length)
            result_label.config(text=f"Generated Password: {password}")

        except ValueError:
            result_label.config(text="Invalid input. Please enter a valid number for password length.")

   
    window = tk.Tk()
    window.title("Password Generator")

   
    Label(window, text="Enter the desired password length:").pack(pady=10)
    length_entry = Entry(window, width=5)
    length_entry.pack(pady=5)

    generate_button = Button(window, text="Generate Password", command=generate)
    generate_button.pack(pady=10)

    result_label = Label(window, text="")
    result_label.pack(pady=10)

    window.mainloop()

generate_password_gui()
