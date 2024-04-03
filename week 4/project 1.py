print("STUDENTS")
females = {
    "EVELYN": (17,5.5,80),
    "JESSICA":(16,6.0,85),
    "SOMTO":(17,5.4,70),
    "EDITH":(18,5.9,60),
    "LIZA":(16,5.6,76),
    "MADONNNA":(18,5.5,66),
    "WAJE":(17,6.1,87),
    "TOLA":(20,6.0,95),
    "AISHA":(19,5.7,50),
    "LATIFA":(17,5.5,49)       
}

males = {
    "chinedu":(19,5.7,74),
    "Liam":(16,5.9,87),
    "Wale":(18,5.8,75),
    "Gbenga":(17,6.1,68),
    "Abiola":(20,5.9,66),
    "Kola":(19,5.5,78),
    "Kunle":(16,6.1,87),
    "George":(18,5.4,98),
    "Thomas":(17,5.8,54),
    "Wesley":(19,5.7,60)
}

for name in females:
    tuple = females[name]
    print(f"NAME is {name}| AGE is {tuple[0]}| HEIGHT is {tuple[1]}| SCORE is {tuple[2]}")