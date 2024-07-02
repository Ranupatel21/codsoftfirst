# Create a project directory and set up a virtual environment.
mkdir todo_app
cd todo_app
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
# Create a file named todo_cli.py.
# todo_cli.py

import sys

tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})

def update_task(index, new_task):
    if 0 <= index < len(tasks):
        tasks[index]["task"] = new_task

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

def view_tasks():
    for idx, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Pending"
        print(f"{idx}. {task['task']} [{status}]")

def main():
    while True:
        command = input("Enter command (add, update, complete, delete, view, exit): ").strip()
        if command == "add":
            task = input("Enter task: ").strip()
            add_task(task)
        elif command == "update":
            index = int(input("Enter task index: ").strip())
            new_task = input("Enter new task: ").strip()
            update_task(index, new_task)
        elif command == "complete":
            index = int(input("Enter task index: ").strip())
            complete_task(index)
        elif command == "delete":
            index = int(input("Enter task index: ").strip())
            delete_task(index)
        elif command == "view":
            view_tasks()
        elif command == "exit":
            break
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()
# Create a file named todo_gui.py.
# todo_gui.py

import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=40)
        self.task_entry.grid(row=0, column=0, padx=10)

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1)

        self.tasks_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.tasks_listbox.grid(row=1, column=0, columnspan=2, pady=10)

        self.complete_button = tk.Button(self.frame, text="Complete Task", command=self.complete_task)
        self.complete_button.grid(row=2, column=0, sticky="ew")

        self.delete_button = tk.Button(self.frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, sticky="ew")

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_tasks_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def complete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index]["completed"] = True
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task.")

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task["completed"] else "Pending"
            self.tasks_listbox.insert(tk.END, f"{task['task']} [{status}]")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
python todo_gui.py




