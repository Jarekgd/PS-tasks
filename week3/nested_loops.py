# Activity 1: Nested Loop

print("How many rows should I have?")
rows = int(input())
print("\nHow many columns should I have?")
cols = int(input())
print("\nHere I go:")
for i in range(rows, 0, 1):
    for j in range(cols,0,1):
        print(":-)", end="")
    print("")