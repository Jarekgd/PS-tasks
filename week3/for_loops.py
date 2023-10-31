# Activity 1: Simple Loop

count = int(input("How many mountains should I display?\n"))
for count in range(0,count,1):
    print("      _")
    print("     / \\_")
    print("    /^    \\")
    print("   / ^     \\_")
    print(" _/ ^ ^     ^\\")
    print("/  ^    ^     \\")

print("\nDone!")

#################################
# Activity 2: Count Down

distance = int(input("How far are we from the target?\n"))
for i in range(distance, 0 , -1):
    print(f"{i} steps remaining")

print("\nTarget achieved!")

###################################
# Activity 3: Range

level = int(input("What level of brightness is required?\n"))
print("Adjusting brightness...\n")

for i in range(0, level + 1, 2):
    print("*" * i)

print("Complete!")

###################################
# Activity 4: Characters

print("\nWhat word do you see?")
word = input()
print("Displaying index positions...\n")

for i in range(0, len(word), 1):
    print(f"index {i}: {word[i]}")

print("\nDone!")
