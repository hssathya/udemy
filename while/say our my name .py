name = input("What is your name? ")
while name != "":
    for x in range(100):
        print(name, end = " ")
    print()   # After the for loop, skip down to the next line
    name = input("Type another name, or just hit [ENTER] to quit: ")
print("Thanks for playing!")
