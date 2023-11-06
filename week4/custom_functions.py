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