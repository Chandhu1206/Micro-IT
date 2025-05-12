import tkinter as tk 
from tkinter import messagebox 
 
def add_task(): 
    task = task_entry.get() 
    if task: 
        task_listbox.insert(tk.END, task) 
        task_entry.delete(0, tk.END) 
    else: 
        messagebox.showwarning("Warning", "Task cannot be empty!") 
 
def mark_done(): 
    try: 
        selected_task_index = task_listbox.curselection()[0] 
        task = task_listbox.get(selected_task_index) #Corrected variable name 
        task_listbox.delete(selected_task_index) 
        task_listbox.insert(tk.END, f"Done: {task}") #Added a colon and space for better readability 
    except IndexError: 
        messagebox.showwarning("Warning", "Select a task to mark as done!") 
 
def delete_task(): 
    try: 
        selected_task_index = task_listbox.curselection()[0] 
        task_listbox.delete(selected_task_index) 
    except IndexError: 
        messagebox.showwarning("Warning", "Select a task to delete!") 
 
root = tk.Tk() 
root.title("TO-DO List") 
root.geometry("400x400") #Corrected geometry string 
 
task_entry = tk.Entry(root, width=40) 
task_entry.pack(pady=10) 
 
add_button = tk.Button(root, text="ADD TASK", command=add_task) #Corrected command 
add_button.pack() 
 
task_listbox = tk.Listbox(root, width=50, height=10) 
task_listbox.pack(pady=10) 
 
done_button = tk.Button(root, text="MARK AS DONE", command=mark_done) #Changed to uppercase for consistency 
done_button.pack() 
 
delete_button = tk.Button(root, text="DELETE TASK", command=delete_task) #Changed to uppercase for consistency 
delete_button.pack() 
root.mainloop() 