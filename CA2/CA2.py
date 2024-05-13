import tkinter as tk
from tkinter import messagebox as mssge


def rice_pasta():
        window =  tk.Toplevel(root)
        window.title("order from rice/pasta")
        window.geometry("500x500")
       
        def order():
                food_name = input_entry.get()  
                if food_name in food_dict:
                        price = food_dict[food_name]
                        quantity = int(quantity_entry.get()) 
                        total.append(price * quantity)
                        mssge.showinfo("Order Placed", f"Order for {food_name} x{quantity} placed successfully!")
                else:
                        mssge.showerror("Error", "Item not found in the menu!")


        
        food_dict= {"Jollof_rice" :350, "Coconut_Fried_rice" : 350,"Jollof_spaghetti" : 350}
        food= ["Jollof  rice = N350\n", "Coconut Fried rice = N350\n","Jollof spaghetti = N350\n",]
        for i in food:
                food_1= tk.Label(window, text=i)
                food_1.pack()
        
        rwriting= tk.Label(window, text="Please put an underscore'_', instead of a space. Thank you")
        rwriting.pack()
      
        input_1 = tk.Label(window, text="order")
        input_1.pack()
        input_entry= tk.Entry(window)
        input_entry.pack()
        
        quantity = tk.Label(window, text="How  many portions?")
        quantity.pack()
        quantity_entry= tk.Entry(window)
        quantity_entry.pack()

        button_order = tk.Button(window, text="Place Order", command=order)
        button_order.pack()
        
def protiens():
        window =  tk.Toplevel(root)
        window.title("order from protiens")
        window.geometry("500x500")
        
        def p_order():
                pfood_name = input_2_entry.get()  
                if pfood_name in pfood_dict:
                        pprice = pfood_dict[pfood_name]
                        pquantity = int(quantity_2_entry.get()) 
                        total.append(pprice * pquantity)
                        mssge.showinfo("Order Placed", f"Order for {pfood_name} x{pquantity} placed successfully!")
                else:
                        mssge.showerror("Error", "Item not found in the menu!")
        
        pfood_dict= {"Sweet_chill_chicken" :1300, "Grilled_chicken_wings" : 400,"Fried_beef" :400, "Fried_fish": 500, "Boiled_Egg":200, "Salted_Sausages":200}
        food= ["Sweet chill chicken = N1300\n", "Grilled chicken wings = N400\n","Fried beef = N400\n", "Fried fish = N500\n", "Boiled Egg = N200\n", "Salted Sausages = N200\n"]
        for i in food:
                food_1= tk.Label(window, text=i)
                food_1.pack()
        writing= tk.Label(window, text="Please put an underscore'_', instead of a space. Thank you")
        writing.pack()
      
        input_2 = tk.Label(window, text="order")
        input_2.pack()
        input_2_entry= tk.Entry(window)
        input_2_entry.pack()
        
        quantity_2 = tk.Label(window, text="How  many?")
        quantity_2.pack()
        quantity_2_entry= tk.Entry(window)
        quantity_2_entry.pack()

        button_order = tk.Button(window, text="Place Order", command=p_order)
        button_order.pack()
                       
def side_dish():
        window =  tk.Toplevel(root)
        window.title("order fromside dishes")
        window.geometry("500x500")
        def s_order():
                sfood_name = input_3_entry.get()  
                if sfood_name in sfood_dict:
                        sprice = sfood_dict[sfood_name]
                        squantity = int(quantity_3_entry.get()) 
                        total.append(sprice * squantity)
                        mssge.showinfo("Order Placed", f"Order for {sfood_name} x{squantity} placed successfully!")
                else:
                        mssge.showerror("Error", "Item not found in the menu!")
        
        
        sfood_dict= {"Savoury_beans" :350, "Roested_Sweet_Potatoes" : 300,"Fried_Plantains" :150, "Mixed_vegetables_and_salad": 150, "Boiled_Yam":150,}
        food= ["Savoury beans = N350\n", "Roested Sweet Potatoes = N300\n","Fried Plantains = N150\n", "Mixed vegetables and salad = N150\n", "Boiled Yam = N150\n"]
        for i in food:
                food_1= tk.Label(window, text=i)
                food_1.pack()
        
        swriting= tk.Label(window, text="Please put an underscore'_', instead of a space. Thank you")
        swriting.pack()

        
        input_3 = tk.Label(window, text="order")
        input_3.pack()
        input_3_entry= tk.Entry(window)
        input_3_entry.pack()
        
        quantity_3 = tk.Label(window, text="How  many?")
        quantity_3.pack()
        quantity_3_entry= tk.Entry(window)
        quantity_3_entry.pack()

        button_order = tk.Button(window, text="Place Order", command=s_order)
        button_order.pack()

def swallows():
        window =  tk.Toplevel(root)
        window.title("order from Swallows and soups")
        window.geometry("500x500")
        def sw_order():
                swfood_name = input_4_entry.get()  
                if swfood_name in swfood_dict:
                        swprice = swfood_dict[swfood_name]
                        swquantity = int(quantity_4_entry.get()) 
                        total.append(swprice * swquantity)
                        mssge.showinfo("Order Placed", f"Order for {swfood_name} x{swquantity} placed successfully!")
                else:
                        mssge.showerror("Error", "Item not found in the menu!")
        
        
        swfood_dict= {"Eba" :100, "Poundo_Yam" : 100,"Semo" :100, "Atama_soup": 450, "Egusi_soup":450,}
        food= ["Eba = N100\n", "Poundo_Yam = N100\n","Atama_soup = N450\n", "Egusi soup= N450\n"]
        for i in food:
                food_1= tk.Label(window, text=i)
                food_1.pack()
        
        swriting= tk.Label(window, text="Please put an underscore'_', instead of a space. Thank you")
        swriting.pack()

        
        input_4 = tk.Label(window, text="order")
        input_4.pack()
        input_4_entry= tk.Entry(window)
        input_4_entry.pack()
        
        quantity_4 = tk.Label(window, text="How  many?")
        quantity_4.pack()
        quantity_4_entry= tk.Entry(window)
        quantity_4_entry.pack()

        button_order = tk.Button(window, text="Place Order", command=sw_order)
        button_order.pack()

def Beverages():
        window =  tk.Toplevel(root)
        window.title("order from Beverages")
        window.geometry("500x500")
        def B_order():
                bfood_name = input_5_entry.get()  
                if bfood_name in bfood_dict:
                        bprice = bfood_dict[bfood_name]
                        bquantity = int(quantity_5_entry.get()) 
                        total.append(bprice * bquantity)
                        mssge.showinfo("Order Placed", f"Order for {bfood_name} x{bquantity} placed successfully!")
                else:
                        mssge.showerror("Error", "Item not found in the menu!")
        
        
        bfood_dict= {"Water" :200, "Glass_Drink_(35cl)" : 100,"PET_Drink_(30cl)" :300, "PET_Drink_(35cl)": 350, "Glass/Canned_Malt":500, "Pineapple_Juice":350, "Mango_Juice":350, "Zobo_Drink":350}
        food= ["Water = N200\n", " Glass_Drink_(35cl) = N100\n","PET_Drink_(30cl) = N300\n", "PET_Drink_(35cl) = N350\n", "Glass/Canned_Malt = N150\n", "Pineapple Juice = N350", "Mango Juice = N350", "Zobo Drink = N350"]
        for i in food:
                food_1= tk.Label(window, text=i)
                food_1.pack()
        
        swriting= tk.Label(window, text="Please put an underscore'_', instead of a space. Thank you")
        swriting.pack()

        
        input_5 = tk.Label(window, text="order")
        input_5.pack()
        input_5_entry= tk.Entry(window)
        input_5_entry.pack()
        
        quantity_5 = tk.Label(window, text="How  many?")
        quantity_5.pack()
        quantity_5_entry= tk.Entry(window)
        quantity_5_entry.pack()

        button_order = tk.Button(window, text="Place Order", command=B_order)
        button_order.pack()

def intro(user_entry):
        new=tk.Toplevel()
        new.minsize(800, 800)
        new.maxsize(900, 900)
        new.title("PAU Cafetaria")

        custom_font = ("calibri", 12, "bold")
        text_1_content = (f"Hey there {user_entry},Welcome to the PAU Cafetaria")
        text_1= tk.Label(new, text=text_1_content)
        text_1.grid(row=0, column=2)


        text_2_content= "MENU"
        text_2= tk.Label(new, text=text_2_content)
        text_2.grid(row=1, column=2)

        text_3_content= ("RICE/PASTA\n" 
                        "Jollof  rice = N350\n" 
                        "Coconut Fried rice = N350\n" 
                        "Jollof spaghetti = N350\n")
                  

        text_4_content= ("PROTEINS\n" 
                        "Sweet Chill Chicken = N1300\n" 
                        "Grilled Chicken wings = N400\n" 
                        "Fried beef = N400\n" 
                        "Fried  Fish = N500\n" 
                        "Boiled Egg = N200\n" 
                        "Salted Sausages = N200\n")

        text_3 = tk.Label(new, text=text_3_content,font=custom_font, wraplength=500, justify="left")
        text_4 = tk.Label(new, text=text_4_content, font=custom_font,wraplength=500, justify="left")
        text_3.grid(row=2, column=0)
        text_4.grid(row=2, column=1)

        button_1 = tk.Button(new, text="Order from RICE/PASTA", command=rice_pasta)
        button_2 = tk.Button(new, text="Order from PROTEINS",command=protiens)

        button_1.grid(row=3, column=0)
        button_2.grid(row=3, column=1)


        text_5_content = ("SIDE DISHES\n"
                        "Savoury Beans = N350\n"
                        "Roested Sweet Potatoes = N300\n"
                        "Fried Plantains = N150\n"
                        "Mixed vegetables and salad = N150\n"
                        "Boiled Yam = N150\n")

        text_6_content= ("SWALLOWS AND SOUPS\n"
                        "Eba = N100\n"
                        "Poundo Yam = N100\n"
                        "Semo = N100\n"
                        "Atama soup = N450\n"
                        "Egusi soup = N450\n")

        text_7_content =  ("BEVERAGES\n"
                            "Water = N200\n"
                            "Glass Drink(35cl) = N100\n"
                            "PET Drink = N300\n"
                            "PET Drink = N350\n"
                            "Glass/Canned Malt = N500\n"
                            "Pineapple Juice = N350\n"
                            "Mango Juice = N350\n"
                            "Zobo Drink = N350\n")

        text_5 = tk.Label(new, text=text_5_content,font=custom_font)
        text_6 = tk.Label(new, text=text_6_content,font=custom_font)
        text_7 = tk.Label(new, text=text_7_content,font=custom_font)
        text_5.grid(row=2, column=2)
        text_6.grid(row=4, column=0)
        text_7.grid(row=4, column=1)

        button_3 = tk.Button(new, text="Order from SIDE DISHES", command=side_dish)
        button_4 = tk.Button(new, text="Order from SWALLOWS  AND SOUPS", command=swallows)
        button_5 = tk.Button(new, text= "ORDER FROM BEVERAGES", command=Beverages)

        button_3.grid(row=3, column=2)
        button_4.grid(row=5, column=0)
        button_5.grid(row=5, column=1)
        
        button_6 = tk.Button(new,text="Proceed to checkout", command=total_calculator)
        button_6.grid(row=5, column=2)
        button_9 = tk.Button(new)
root=tk.Tk()
root.title("Provide name")
root.geometry("200x200")


input_entry = None
quantity_entry = None

total = []
def total_calculator():
        all =  sum(total)
             

        if all > 2500  and all< 5000:
                e= all *0.15
                w = all - e
                mssge.showinfo("balance",f"Total Balance  is N{w}\n Thank you, please come again")
        elif all > 5000:
                o=all *0.25
                d = all - o
                mssge.showinfo("balance",f"Total Balance is N{d}\n Thank you, please come again")
        elif all == 0:
                mssge.showerror("balance","There is no total balance as you didnt order anyting")       
        
        else :
                p = all *0.1
                ans = all - p
                mssge.showinfo(f"balance",f"Total Balance is N{ans}\n Thank you, please come again")
        
username = tk.Label(root,text="Student/Staff name")
username.pack()
user_entry=tk.Entry(root) 
user_entry.pack()

button = tk.Button(root, text="submit", command=lambda: intro(user_entry))
button.pack()




root.mainloop()