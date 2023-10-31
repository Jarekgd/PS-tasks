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
        break
a=i
for i in range(0, len(seq), 1):
    if seq[i] == mark:
        continue
b=i-1
print(f"The distance between the markers is {b-a}.")






