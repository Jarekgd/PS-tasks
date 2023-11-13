# Activity 1: Simple Tuple

def likelihood():
    likehoods=(50, 38, 27, 99, 4)
    return min(likehoods)

def run_task1():
    value=likelihood()
    print(f"Minimum likelihood of falling: {value}%")

run_task1()

#####################################
# Activity 2: Tuple Return Type
print("")
def likelihood_min_max():
    likelihoods=(50, 38, 27, 99, 4)
    minim=min(likelihoods)
    maxim=max(likelihoods)
    return minim, maxim

def run_task2():
    minim, maxim=likelihood_min_max()
    print(f"Minimum likelihood of falling: {minim} %")
    print(f"Maximum likelihood of falling: {maxim} %")

run_task2()