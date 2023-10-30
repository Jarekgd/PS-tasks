# Activity 1: Simple loop

print("How many apples should I remove?")
apples = int(input())
while apples > 0:
    print("Removed apple.")
    apples -= 1

######################################
# Activity 2: Count

print("How many obstacles must I avoid?")
obstacles = int(input())
count = 1
while count <= obstacles:
    print("Avoiding...Done! ", end="")
    print(f"{count} obstacles avoided.")
    count += 1
print("\nAll obstacles have been avoided.")