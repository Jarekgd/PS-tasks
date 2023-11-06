print("built_in_functions.py")
letter = input("Please enter a letter:\n")

if len(letter) == 1:
    print(f"The ASCII code for {letter} is {ord(letter)}.")
else:
    print("Too many letters!")
print("Program Ended!")