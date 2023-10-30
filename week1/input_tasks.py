# Activity 1
# Ask user to enter their name

print("What is your name?")
name = input()
print(f"It is nice to meet you {name}")

# name = input("What is your name?")
# print(f"It is nice to meet you {name}")

# Activity 2: ASCII Robot
print("\nPlease enter a character for the eye")
eye = input()
print("")
print("  \\     /")
print("   \\   /")
print("###########")
print("#         #")
print(f"#  {eye}   {eye}  #")
print("#         #")
print("#  =====  #")
print("###########")
print("   #  #")

# Activity 3: Data Types
print("\nWhat is your name?")
name = input()
print("How old are you?(in years)")
age = int(input())
print("How tall are you (in meters)?")
height = float(input())
print("How much do you weigh (in kilograms)?")
weight = int(input())
bmi = weight / (height**2)
print(f"{name} you are {age} years old and your BMI is {bmi:.2f}")

# parenthesis are not required, exponent has priority before divide and multiply, but it is good for more readable  code

# exponents can be done in different ways:
# a = pow(height,2)
# or
# import math
# a = math.pow(height,2)
# or
# import numpy as np
# a = np.power(height, 2)

# other way of formatting floats:
# round(a, 2)
# or
# bmi_formated = "{:.2f}".format(bmi)
# or
# bmi_formated = format(bmi, ".2f")


