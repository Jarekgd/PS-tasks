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

###########################################
# Activity 3: IF...ELIF...ELSE statement

direct = input("Towards which direction should I go (up, down, left or right)?\n")
if direct == "up":
    print("I am moving in an upwards direction!")
elif direct == "down":
    print("I am moving in a downwards direction!")
elif direct == "left":
    print("I am moving in a left direction!")
else:
    print("I am moving in a right direction!")

#########################################
# Activity 4: Modulo Operator

print("Please enter a whole number.")
num = int(input())
if num % 2:
    print(f"The number {num} is an odd number.")
else:
    print(f"The number {num} is an even number.")

# there is no need to write if num % 2 == 1 , 1 means the value of boolean it true, 0 is false.

#########################################
Activity 5: Comparison Operators

print("Please enter the first number.")
num1 = int(input())
print("Please enter the second number.")
num2 = int(input())
if num1 > num2:
    print("The second number is the smallest.")
elif num1 < num2:
    print("The first number is the smallest.")
else:
    print("Both are equal!")