import tkinter as tk
from tkinter import messagebox as mssge


    
    



root = tk.Tk()
label =tk.Label(root, text = "Welcome to the checkout page!\n")
label.pack()
root.title("Checkout page")
root.geometry("500x400")




    
label_1 = tk.Label(root, text = "please input the weight(kg) and place of your delivery :)")
label_1.pack()
    
weight_label = tk.Label(root, text = "weight")
weight_label.pack()
weight_input = tk.Entry(root)
weight_input.pack()
    
location_label = tk.Label(root, text = "Location")
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack()



def price_checker():
    weight = int(weight_input.get())
    location = location_entry.get()
    if location == "ibeju lekki community":
            if weight >= 10:
                mssge.showinfo("info", "Total purchase is N5,000")
            else:
                mssge.showinfo("info", "Total purchase is N3,500")
    elif location == "epe":
        if weight >= 10:
            mssge.showinfo("info", "Total purchase is N10,000 ")
        else:
            mssge.showinfo("info", "Total purchase is N5,000")
    else:
        mssge.showerror("error", "Delivery services not available in your location :(")

proceed_button = tk.Button(root, text = "Proceed", command = price_checker)
proceed_button.pack()

root.mainloop()