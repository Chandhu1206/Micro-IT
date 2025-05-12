import tkinter as tk 
import random 
import string 

def generate_password(): 
 length= int(entry.get()) 
 password= ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length)) 
 password_label.config(text=password) 

def copy_password(): 
 root.clipboard_clear() 
 root.clipboard_append(password_label.cget("text")) 
 root.update() 

root=tk.Tk() 
root.title("Password Generator") 

tk.Label(root,text="Enter Password Length:").pack() 
entry=tk.Entry(root) 
entry.pack() 

generate_button= tk.Button(root,text="Generate", command=generate_password) 
generate_button.pack() 

password_label=tk.Label(root,text="",font=("Arial",14)) 
password_label.pack() 

copy_button= tk.Button(root, text="Copy Password", command=copy_password) 
copy_button.pack() 
root.mainloop() 