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
def display_chars(path, chars):
    with open(path + "/library.txt") as f:           # open and close file when done, absolute path to the file
        print(f"The first {chars} characters are:")
        print(f.read(chars))

def display_line(path):
    with open(path + "/library.txt") as f:
        print("\nThe first line is:")
        print(f.readline())

def display_text(path):
    f=open(path+"/library.txt")                # open file, default = for reading, default = text format
    print("\nThe full text is:")
    print(f.read())
    f.close()                   # close file

def run_task2():
    display_chars(os.getcwd(), 5)
    display_line(os.getcwd())
    display_text(os.getcwd())

if __name__ == "__main__":
    run_task2()

###########################################
# Activity 3: Reading a File
print("")

def search(file):
    print("Searching...")
    with open(file) as f:
        for line in f:
            location=line.strip()       # separating lines
            print(f"Looked in {location}")
    print("...Done!")
    f.close()

def run_task3():
    search("library.txt")

if __name__ == "__main__":
    run_task3()