# Activity 1: Nested Decision

print("What type of cover does the book have?")
cover = input()

if cover == "soft":
    print("Is the book perfect-bound?")
    bound = input()
    if bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books" )
else:
    print("Books with hard covers can be more expensive!")

########################################################
# Activity 2: Multiple Nested Decisions

print("Where should I look?")
room = input()
if room == "in the bedroom":
    print("Where in the bedroom should I look?")
    place = input()
    if place == "under the bed":
        print("Found some shoes but no phone")
    else:
        print("Found some mess but no phone.")
elif room == "in the bathroom":
    print("Where in the bathroom should I look?")
    place = input()
    if place == "in the bathtub" :
        print("Found a rubber duck but no phone")
    else:
        print("Found bathroom stuff but no phone.")

elif room == "in the living room":
    print("Where in the living room should I look?")
    place = input()
    if place == "in the bathtub" :
        print("Yes! I found my phone!")
    else:
        print("Found some stuff but no phone.")
else:
    print("I do not know where that is but I will keep looking.")

