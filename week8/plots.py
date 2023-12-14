# Activity 1: Simple Line Plot
import random
import matplotlib.pyplot as plt

def display_line(x, y):
    plt.plot(x, y)
    plt.show()

def run_task1():
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    plt.xlabel("x values")
    plt.ylabel("y values")
    display_line(x_values, y_values)

# run_task1()


#################################################
# Activity 2: Squares with Line Plot

def small():
    x = [3, 4, 4, 3, 3]
    y = [4, 4, 3, 3, 4]
    plt.plot(x, y, 'ro:')



def medium():
    x = [2, 5, 5, 2, 2]
    y = [5, 5, 2, 2, 5]
    plt.plot(x, y, 'gs--')



def large():
    x = [1, 6, 6, 1, 1]
    y = [6, 6, 1, 1, 6]
    plt.plot(x, y, 'bx-')



def run_task2():
    small()
    medium()
    large()
    plt.show()

# run_task2()

##############################
# Activity 3: Path with Line Plots

def coordinate():
    x = int(input("Gimme x value!"))
    y = int(input("Gimme y value!"))
    return (x, y)

def path():
    print("Retrieving path...")
    x_values = []
    y_values = []
    for i in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
    return [x_values, y_values]


def run_task3():
    values = path()
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.plot(values[0], values[1], 'ro--')
    plt.show()

# run_task3()

#####################################
# Activity 4: Data Dictionary and Plots

def data():
    paths = {}
    line = input("What type of line? ':', '--', or '-'")
    colour = input("What colour? 'r', 'g', or 'b'")
    marker= input("What marker type? 'o', 's', or '^'")
    paths["line"]=line
    paths["colour"]=colour
    paths["marker"]=marker
    return paths

def generate():
    number = int(input("How many lines would you like to display?"))
    values = data()
    x_values = []
    y_values = []
    for i in range(number):
        x_values.append(random.sample(range(1,20), 1))
        y_values.append( random.sample(range(1,20), 1))
    plt.plot(x_values, y_values, f"{values["colour"]}{values["marker"]}{values["line"]}")
    plt.show()
def run_task4():
    print("Running....")
    generate()
    print("Done!")

run_task4()
