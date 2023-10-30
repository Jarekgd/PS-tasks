# Activity 1: Logical OR Operator

print("What type of adventure should I have?")
type = input()
if (type == "scary") or (type == "short"):
    print("Entering the dark forest!")
elif (type == "safe") or (type == "long"):
    print("Taking the safe route!")
else:
    print("Not sure which route to take." )

####################################
# Activity 2: Logical AND operator

print("What did I hear?")
hear = input()
print("\nWhat did I see?")
see = input()
if (hear == "grrr") and (see == "two red eyes"):
    print("There is a scary creature. I should get out of here!")
else:
    print("I am a little scared but I will continue!")
