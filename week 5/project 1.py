import tkinter as tk
import csv
from tkinter import messagebox as mssgebx
def intro(name):
    window = tk.Toplevel(root)
    window.title = ("Admin PO")
    window.geometry = ("500x400")
    
    labael_1 = tk.Label(window, text = f"welcome back {name}.Its nice to have you\n")
    labael_1.pack()

def confirm():
    f_name= name_entry.get()
    dept = dept_entry.get()
    with open('GIG-logistics.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if f_name in row and dept in row:
                intro(f_name)
            else:
                mssgebx.showerror("error", "wrong name or department")

root= tk.Tk()
root.title("Login to database")
root.geometry("400x200")

dept_label = tk.Label(root, text="Department:")
dept_label.pack()
dept_entry = tk.Entry(root)
dept_entry.pack()

name_label = tk.Label(root, text="First Name:")
name_label.pack()
name_entry = tk.Entry(root)  
name_entry.pack()

enter_button = tk.Button(root, text = "enter", command= confirm )
enter_button.pack()
root.mainloop()