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

################################
# Activity 3: Review

print("Pet Store")
print("Do you have a pet?(y/n)")
doYou = input()
if doYou == "y":
    print("How many pets do you have?")
    howMany = int(input())
    if howMany > 1:
        print(f"You have {howmany} pets! Wow!")
        print("What pets do you have? (dogs/ cats/ fish")
        whatKind = input()
        if (whatKind == "dogs") or ( whatKind == "cats"):
            print(f"I love {}! They are good friends")
        elif whatKind == "fish":
            print(f"I love fish. They don't bark!")
    elif howMany == 1:
        print("One is good, but buy more!")
        print("What do you have?(dog/cat/fish")
        whatKind = input()
        if (whatKind == "dog") or ( whatKind == "cat"):
            print(f"I love {}! They are good friends")
        elif whatKind == "fish":
            print("you have only one fish? What a shame!")
    else:
        print("C'mon! You should get a pet!")
else:
    print("You must have a pet! You live will be better!")
