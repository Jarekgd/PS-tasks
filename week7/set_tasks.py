# Activity 1: Simple Set
def observed():
    observations = {"Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"}
    return observations


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
    print("\nCounting observations...")
    ob = observed_items()
    s = set()
    for i in ob:
        s.add((i, ob.count(i)))
    print("")
    for i in s:
        print(f"{i[0]} observed {i[1]} times.")


run_task2()
