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