# Activity 1: IF statement

type = input("What type of book is this?\n")
if type == "adventure":
    print(f"\nI like {type} books!\n")
print("Finished reading book.")

#############################################
# Activity 2: IF...ELSE statement

activity = input("Please enter the activity to be performed.\n")
if activity == "calculate":
    print(f"\nPerforming calculations...\n")
else:
    print("Performing activity...")
print("Activity completed!")