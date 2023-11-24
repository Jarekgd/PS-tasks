# Activity 1: Reading a CSV File

import csv

def read_csv(path):
    f=open(path)
    csv_reader=csv.reader(f)
    headings=next(csv_reader)
    print(f"Headings:\n{headings}" )
    print("Values:")
    for values in csv_reader:
        print(values)
    f.close()

if __name__=="__main__":
    read_csv("clothing.csv")