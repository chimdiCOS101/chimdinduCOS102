import tkinter as tk
from tkinter import messagebox as messagebox

def welcomeMessage(username):
    window  = tk.Toplevel(root)
    window.title("Admin Box")
    window.geometry("500x200")
    
    label_1 = tk.Label(window, text = f"welcome  {username}\n")
    label_1.pack()
    label_2 = tk.Label(window, text = "This is phython tkinter with GUI")
    label_2.pack()
    
    

    
def submit():
    username=username_entry.get()
    password=password_entry.get()
    
    if username ==  "Mary" and password == "cos102":
        welcomeMessage(username)
    else:
        messagebox.showerror("Login", "Invalid username or password")

root = tk.Tk()
root.title("Login")
root.geometry("300x150")

# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # Show * instead of plain text
password_entry.pack()

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

root.mainloop()