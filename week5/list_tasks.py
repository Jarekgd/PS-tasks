# Activity 1: Simple List
def directions():
    steps=["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps

def run_task1():
    print(directions())

if __name__ == "__main__":
    run_task1()

####################################
# Activity 2: Indexing
print("")
def movements():
    path=["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

def run_task2():
    print("Moving...")
    path = movements()

##################################
# Activity 4: Populate

    for i in range(0,len(path),2):
        direction = path[i]
        steps = path[i + 1]
        print(f"{direction} for {steps} steps")
        i += i

run_task2()

######################################
# Activity 3: Iterate
print("")
def menu():
    print("Please select a direction:")
    steps=directions()
    for i in range(len(steps)):
        print(f"{i}: {steps[i]}")

def run_task3():
    menu()

run_task3()

#####################################
# Activity 4: Populate

def menu_and_input():
    print("\nPlease select a direction:")
    direction=directions()
    for i in range(len(direction)):
        print(f"{i}: {direction[i]}")
    step=int(input())
    return direction[step]

def run_task4():
    print("\nWorking out escape route...")
    route=[]
    for i in range(5):
        route.append(menu_and_input())
    print(f"Escape route: {route}" )

run_task4()
