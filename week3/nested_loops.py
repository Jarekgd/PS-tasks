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

##################################
# Activity 2: Nesting

print("Please enter a sequence")
seq = input()
print("Please enter the character for the marker")
mark = input()
for i in range(0, len(seq), 1):
    if seq[i] == mark:
        break               # loop stops at the first x
a=i                         # first x position saved as a
for i in range(a+1, len(seq), 1):   # next loop starts after first x
    if seq[i] == mark:
        break               # loop stops at the second x
b=i-1                       # second x position saved as b
print(f"\nThe distance between the markers is {b-a}.")






