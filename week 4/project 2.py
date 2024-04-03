intro = "izifin Technology"
print(intro.upper)
YOE = int(input("give me your working years of experience (i.e how long you have been working in this field)"))
print("\n next")
age = int(input("how  old are you?"))
if YOE > 25 and age >= 55:
    print("Annual Tax Revenue (ATR) is N5,600,000")
elif YOE > 20 and age >= 45:
    print("Annual Tax Revenue (ATR) is N4,800,000")
elif YOE > 10 and age >= 35:
        print("Annual Tax Revenue (ATR) is N1,500,000")
else:
       print("Annual Tax Revenue (ATR) is N550,000")




    