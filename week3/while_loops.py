import time
# Activity 1: Simple loop

def simple_loop():
    print("How many apples should I remove?")
    apples = int(input())
    while apples > 0:
        print("Removed apple.")
        apples -= 1

######################################
# Activity 2: Count
def count():
    print("How many obstacles must I avoid?")
    obstacles = int(input())
    count = 1
    while count <= obstacles:
        print("Avoiding...Done! ", end="")
        print(f"{count} obstacles avoided.")
        count += 1
    print("\nAll obstacles have been avoided.")

######################################
# Activity 3: ASCII
def ascii():
    i = 1
    print("How many bars should be charged?")
    bars = int(input())
    print("")
    while i <= bars:
        print("Charging:", end="")
        print(" \u2588" * i)
        time.sleep(0.5)
        i += 1

######################################
# Activity 4: Repeating Word
def repeating_word():
    print("Please enter a phrase:")
    phrase = input()
    i = 1
    while i <= len(phrase):
        print("Hi ", end ="")
        i += 1

# print("Hi " * phrase)

#####################################
# Activity 5: Sum 100
def sum_100():
    print("Calculating the sum of the first 100 numbers...")
    i = 1
    sum = 0
    while i <= 100:
        sum = sum + i
        i += 1

    print(f"...Done! The answer is {sum}.")

###################################
# Activity 6: Sum User Numbers
def sum_user_numbers():
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
