intro = "interest calculator"
print(intro.upper())

print("CHOOSE  WHAT YOU WANT ME  TO CALCULATE")

choice = int(input(" 1. simple interest"
                   "\n 2. compound interest"
                   "\n 3. annuity plan"))
prin = int(input("Principal amount = "))
rate = int(input(" How  much Rate? "))
time = int(input("How much time? "))

if choice == 1:
    print("FORMULA FOR SIMPLE INTEREST A=P(1+(R/100)T)")

    Amount = prin * (1 + (rate / 100) * time)

    print(Amount)
elif choice == 2:
    print("FORMULA FOR COMPOUND INTEREST A=P(1+R/n)nt")
    no = int(input("what is the value of 'n' in the formula above? "))
    Amm = prin * (1+rate/no) * (no*time)
    print(Amm)
elif choice == 3:
    print("FORMULA FOR ANNUITY PLAN PMT= [(1 + R/n)exp of nt - 1]/ R/n")
    n = int(input("what is the value of 'n' in the formula above? "))
    PMT = ((1 + rate/n) ** (n * time) - 1) / (rate / n)
    print(PMT)
else:
    print("ERROR")


