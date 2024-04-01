
intro = input("do you want to do quadratic or cubic?")
if intro ==  "quadratic":
    a = int(input("give me the coefficient of x2 "))
    b = int(input("give me the coefficient of x "))
    c = int(input("give me the constant "))
    disc = ((b**2) - (4 * a * c))**0.5
    val_1 = (-b + disc) / 2*a
    val_2 = (-b - disc) / 2*a
    print(f"the roots are {val_1} and {val_2}")
else:
    print("no")    
