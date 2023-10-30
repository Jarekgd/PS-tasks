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

######################################
# Added code to demonstrate the use of a while loop with ASCII art.

i = 1
print("How many bars should be charged?")
bars = int(input())
print("")
while i <= bars:
    print("Charging:", end="")
    print(" \u2588" * i)
    i += 1

######################################
# Activity 4: Repeating Word

print("Please enter a phrase:")
phrase = input()
i = 1
while i <= len(phrase):
    print("Hi ", end ="")
    i += 1

# print("Hi " * phrase)

#####################################
# Activity 5: Sum 100

print("Calculating the sum of the first 100 numbers...")
i = 1
sum = 0
while i <= 100:
    sum = sum + i
    i += 1

print(f"...Done! The answer is {sum}.")

###################################
# Activity 6: Sum User Numbers

print("How many numbers should I sum up?")
n = int(input())
i = 1
sum = 0
while i <= n:
    print(f"Please enter number {i} of {n}")
    num = int(input())
    sum = sum + num
    i += 1
print(f"The answer is {sum}.")
