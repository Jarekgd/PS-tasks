# Activity 1: Simple Line Plot
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

run_task2()
