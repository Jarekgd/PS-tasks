# Activity 1: Simple Dictionary

def pattern():
    sequences = {}
    sequences["Short Sequence"] = 3
    sequences["Medium Sequence"] = 2
    sequences["Long Sequence"] = 1
    return sequences


####################################
# Activity 2: Iterate Through Dictionaries


def display_keys(data):
    print()
    print("Keys:")
    for key in data.keys():
        print(key)


def display_values(data):
    print()
    print("Values:")
    for value in data.values():
        print(value)


def display_items(data):
    print()
    print("Pairs:")
    for key, value in data.items():
        print(f"{key} {value}")


def run():
    print("Dictionary:")
    print(pattern())
    display_keys(pattern())
    display_values(pattern())
    display_items(pattern())


run()

##################################
# Activity 3: Dictionary of Dictionaries
print()

def short_pattern():
    pattern = {}
    pattern["sequence"] = "101"
    pattern["occurrences"] = 5
    return(pattern)

def medium_pattern():
    pattern = {}
    pattern["sequence"] = "111000"
    pattern["occurrences"] = 25
    return pattern

def long_pattern():
    pattern = {}
    pattern["sequence"] = "1100110011001100"
    pattern["occurrences"] = 50
    return pattern

def run_task3():
    print("Analysing patterns...")
    s = short_pattern()
    m = medium_pattern()
    l = long_pattern()
    print(s)
    print(m)
    print(l)

run_task3()

