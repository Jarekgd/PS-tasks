# Activity 1: Current Working Directory
import os           # built-in module for interacting with the operating system, it is part of standard module, stdlib

def cwd():
    path=os.getcwd()                # get current working directory method
    print(f"The current working directory is {path}")
    print("The directory contains the following files:")
    for file in os.listdir(path):   # list of files in specific directory
        print(file)

def run():
    print("Processing...")
    cwd()

run()

##########################################
# Activity 2: Reading a File
print("")
def display_chars(file, chars):
    with open(file) as f:           # open and close file when done
        print(f"The first {chars} characters are:")
        print(f.read(chars))

def display_line(path):
    with open(path) as f:
        print("\nThe first line is:")
        print(f.readline())

def display_text(path):
    f=open(path)                # open file, default = for reading, default = text format
    print("\nThe full text is:")
    print(f.read())
    f.close()                   # close file

def run_task2():
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")

run_task2()