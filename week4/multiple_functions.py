# Activity 1: Multiple User Defined Functions

def display_ladder(steps):
    print("\n| |")
    for i in range(steps):
        print("***")
        print("| |")

def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    display_ladder(steps)

# create_ladder()

#############################################
# Activity 2: Return Values

def sum_weights(char_w, invent_w):
    return char_w + invent_w

def calc_avg_weight(char_w, invent_w):
    return sum_weights(char_w, invent_w) / 2

def run():
    print("What is the weight of the person?")
    char_w = float(input())
    print("What is the weight of their inventory?")
    invent_w = float(input())
    print("What would you like to calculate (sum or average)?")
    answer = input()

    suma = sum_weights(char_w, invent_w)
    aver = calc_avg_weight(char_w, invent_w)

    if answer == "sum":
        print(f"The sum of weights is {suma}.")
    if answer == "average":
        print(f"The average of weights is {aver}")

# run()

#################################################
# Activity 3: Word Manipulation
def box(word):
    print(f"******{"*" * len(word)}*******")
    print(f"*     {" " * len(word)}      *")
    print(f"*     {word}      *")
    print(f"*     {" " * len(word)}      *")
    print(f"******{"*" *  len(word)}*******")

def lowercase(word):
    print(word.lower())

def uppercase(word):
    print(word.upper())

def mirror(word):
    reversed = ""
    for i in word:
        reversed = i + reversed
    print(f"{word} | {reversed}")

def repeat(word):
    print("How many times?")
    repeat = int(input())
    for i in range(repeat):
        if i % 2:
            print(word.lower())
        else:
            print(word.upper())
def menu():
    print("Enter a word:")
    word = input()
    print("Choose the option:")
    print("1) Display in a Box")
    print("2) Display Lower-case")
    print("3) Display Upper-case")
    print("4) Display Mirrored")
    print("5) Repeat –  how many times:")
    choice = input()
    if choice == "1":
        box(word)
    elif choice == "2":
        lowercase(word)
    elif choice == "3":
        uppercase(word)
    elif choice == "4":
        mirror(word)
    elif choice == "5":
        repeat(word)
    else:
        print("Wrong input")
# menu()


