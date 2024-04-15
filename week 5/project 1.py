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
    with open('GIG-logistics.csv', 'r') as file:
    names = 

root= tk.Tk()
root.title("Login to database")
root.geometry("400x200")

name_label = tk.Label(root, text="Username:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  
password_entry.pack()


done = tk.Button(root, text = "done")