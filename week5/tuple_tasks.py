# Activity 1: Simple Tuple

def likelihood ():
    likehoods=(50, 38, 27, 99, 4)
    return min(likehoods)

def run_task1():
    value=likelihood()
    print(f"Minimum likelihood of falling: {value}%")

if __name__ == "__main__":
    run_task1()