# Activity 1: Nested Loop

print("How many rows should I have?")
rows = int(input())
print("\nHow many columns should I have?")
cols = int(input())
print("\nHere I go:\n")
for i in range(0, rows, 1):
    for j in range(0, cols, 1):
        print(":-) ", end="")
    print("")