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

####################################
# Activity 3: Nested Tuples
print("")
def steps():
    likelihoods=[("step 1", 50),("step 2", 38),("step 3", 27),("step 4", 99),("step 5", 4)]
    return likelihoods

def run_task3():
    likehood=steps()
    good_steps=[]
    bad_steps=[]
    for i in range(len(likehood)):
        if likehood[i][1] >= 50:
            bad_steps.append(likehood)
        else:
            good_steps.append(likehood)
    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")

run_task3()