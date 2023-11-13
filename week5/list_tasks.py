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

def movements():
    path=["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

def run_task2():
    print("Moving...")
    path = movements()

    for i in range(0,len(path),2):
        direction = path[i]
        steps = path[i + 1]
        print(f"{direction} for {steps} steps")
        i += i

run_task2()