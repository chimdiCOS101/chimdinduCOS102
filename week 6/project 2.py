import tkinter as tk
from tkinter import messagebox as mssge

def done(list):
    print("Button clicked!")
    credit = []
    for i in list:
        if i >= 60 and i <= 100:
            credit.append("pass")
        else:
            credit.append("fail")
    
    gif = 0
    for i in credit:
        if i == "pass":
            gif += 1
        else:
            gif +=0
    if gif == 5:
        text_8 = mssge.showinfo("info",  "Congrats! you have more than 5 credits")
        
    else:
        text_9 = mssge.showerror("error",  "Sorry, your grades do not meet the requirements")    


def computer_science():
    window = tk.Toplevel(root)
    window.title("computer science")
    window.geometry("1000x1000")
    
    

    
    text_3 = tk.Label(window, text= "Here are the requirements to be admitted  ")
    text_3.pack()
    
    text_4 = tk.Label(window, text= " JAMB score of 250 and above \n"
                                    "Have credits in the following subjects:\n" 
                                    "chemistry, physics, math,english, data processing\n"
                                    "Pass the interview \n")
    text_4.pack()
    
    jamb_label = tk.Label(window, text= "JAMB score")
    jamb_label.pack()
    jamb_input = tk.Entry(window)
    jamb_input.pack()
    
    text_5 = tk.Label(window, text= "CREDIT EVALUATION")
    text_5.pack()
    
    
    text_6 = tk.Label(window, text= "A = 80 - 100\n"
                                    "B = 70 - 79\n"
                                    "C = 60 - 69\n"
                                    "D = 50 - 59\n"
                                    "E = 40 - 49\n"
                                    "F = 39 <= \n")
    text_6.pack()
    
    text_7 = tk.Label(window, text= "Enter your Grades here")
    text_7.pack()
    
    storage = []
    subj = {1:"chemistry", 2:"physics", 3:"math", 4:"english", 5:"data processing"}
    count = 0
    for i in range(6):
        count+=1
        grade = tk.Label(window, text= subj[count])
        grade.pack()
        grade_input = tk.Entry(window)
        grade_input.pack()
        storage.append(grade_input)
    
    
    frame = tk.Frame(window, bg = "lightblue", bd = 1, relief = tk.RAISED)
    frame.pack(padx=10, pady=10)
    label = tk.Label(frame, text= "submition button down below", bg= "lightblue")
    label.pack(padx= 10, pady= 10 )
    
    finish = tk.Button(frame, text= "Done", command=lambda: done(storage) )
    finish.pack(padx= 5, pady=  5)
    frame.pack()
    
    
    

      



root = tk.Tk()
root.title("Home page")
root.geometry("500x500")

text = tk.Label(root, text= "Welcome to the Department Placement page \n")
text.pack()

text_2 = tk.Label(root, text= "Choose your desired Department of study \n")
text_2.pack()

comp_sci = tk.Button(root, text= "computer science", command=computer_science)
comp_sci.pack()

mass_comm = tk.Button(root, text= "Mass Communication")
mass_comm.pack()


    

root.mainloop()