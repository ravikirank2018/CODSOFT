import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog, messagebox
import json
from datetime import datetime

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.tasks = []
        self.load_tasks()
        self.create_widgets()

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=2)

    def create_widgets(self):
        self.task_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, height=10, width=40)
        self.task_listbox.pack(pady=10)

        self.refresh_listbox()

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)
        
        self.done_button = tk.Button(self.master, text="Mark as Done", command=self.mark_as_done)
        self.done_button.pack(side=tk.LEFT, padx=5)

        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.destroy)
        self.quit_button.pack(side=tk.RIGHT, padx=5)

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task["done"] else "Not Done"
            self.task_listbox.insert(tk.END, f"{task['title']} - {status}")

    def add_task(self):
        title = simpledialog.askstring("Add Task", "Enter task title:")
        if title:
            new_task = {
                "title": title,
                "done": False,
                "created_at": str(datetime.now())
            }
            self.tasks.append(new_task)
            self.save_tasks()
            self.refresh_listbox()

    def mark_as_done(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.tasks[task_index]["done"] = True
            self.save_tasks()
            self.refresh_listbox()
            messagebox.showinfo("Mark as Done", "Task marked as done.")
        else:
            messagebox.showwarning("Mark as Done", "Please select a task.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
