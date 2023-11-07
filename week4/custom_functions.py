# Activity 1: Simple User Defined Function
def listen():
    print("What sound did you hear?")
    sound = input()
    print(f"That was a loud {sound}!\n")

listen()

#########################################
# Activity 2: Nesting

def identify ():
    print("What lies before us?")
    answer = input()
    if answer == "a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine.")

identify()
print("")
########################################
# Activity 3: Parameters

def escape_by(plan):
    if plan == "jumping over":
        print(f"Can we try {plan}?")
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print(f"\nCan we try {plan}?")
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "cross bridge ahead":
        print(f"\nCan we try {plan}?")
        print("That might just work! Let's go!")
    else:
        print("We cannot escape that way! The boulder is in the way!" )

escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")

############################################
# Activity 4: Loop

def cross_bridge(steps):
    for i in range(steps):
        print("Crossed step.")
    if i >= 5:
        print("The bridge is collapsing!")
    else:
        print("we must keep going!")

cross_bridge(3)
cross_bridge(6)
print("")
##############################################
# Activity 5: Multiple Parameters

def climb_ladder(remaining, crossed):
    if remaining > crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")

climb_ladder(5, 2)
climb_ladder(2, 5)
