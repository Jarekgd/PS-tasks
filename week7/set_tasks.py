# Activity 1: Simple Set
def observed():
    observations = {"Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"}
    return observations

def run_task1():
    s = observed()
    print(s)

run_task1()


#################################
# Activity 2: Set From Other Data Structures

def observed_items():
    observations = []
    for i in range(7):
        print("Please enter an observation:")
        observations.append(input())
    return observations


def observed_items1():
    observations = ["Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"]
    return observations


def run_task2():
    print("\nCounting observations ...")
    ob = observed_items()
    s = set()
    for i in ob:
        s.add((i, ob.count(i)))
    print()
    for i in s:
        print(f"{i[0]} observed {i[1]} times.")


run_task2()

###################################
# Activity 3: Sorting

def observed_items():
    observations = []
    print("Counting observations ...")
    for i in range(5):
        print("Please enter an observation:")
        observations.append(input())
    return observations


def remove_observations():
    ob = observed_items()
    while True:
        print("Do you wish to remove an observation (y/n)?")
        choice = input()
        if choice == "y":
            print("What observation do you wish to remove?")
            print(ob)
            choice1 = input()
            ob.remove(choice1)
            print("Done!")
            print(ob)
        else:
            break
    return ob


def run_task3():
    rem = remove_observations()
    print("Observations:")
    s = set()
    for i in rem:
        s.add((i, rem.count(i)))
    print()
    for i in s:
        print(f"{i[0]} observed {i[1]} times.")


run_task3()



