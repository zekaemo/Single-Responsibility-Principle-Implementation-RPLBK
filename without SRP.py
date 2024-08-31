import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        # Initialize data structure for tasks
        self.tasks = []

        # Create GUI elements
        tk.Label(root, text="Task:").grid(row=0, column=0)
        self.task_entry = tk.Entry(root)
        self.task_entry.grid(row=0, column=1)

        tk.Button(root, text="Add Task", command=self.add_task).grid(row=0, column=2)
        tk.Button(root, text="Delete Selected Task", command=self.delete_task).grid(row=1, column=2)
        tk.Button(root, text="Sort Tasks", command=self.sort_tasks).grid(row=2, column=2)

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=1, column=0, columnspan=2)

        tk.Button(root, text="Mark as Completed", command=self.mark_as_completed).grid(row=2, column=0, columnspan=2)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({'text': task, 'status': 'Pending'})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task!")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            del self.tasks[selected_index[0]]
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete!")

    def mark_as_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks[selected_index[0]]['status'] = 'Completed'
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as completed!")

    def sort_tasks(self):
        self.tasks.sort(key=lambda x: x['status'])
        self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, f"{task['text']} ({task['status']})")

root = tk.Tk()
app = TodoApp(root)
root.mainloop()
