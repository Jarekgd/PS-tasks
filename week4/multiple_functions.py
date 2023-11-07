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

create_ladder()

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

run()