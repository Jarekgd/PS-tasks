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


