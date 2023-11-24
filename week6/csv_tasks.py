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

######################################
# Activity 2: Extract Values from CSV
print("")
def extract(path):
    print("Extracting... ",end="")
    with open(path) as file:
        csv_reader=csv.reader(file)
        headings=next(csv_reader)
        names=""
        for value in csv_reader:
            names+=value[1]+"\n"
    print("Done!")
    print("Done! The extracted items are:")
    print(names)

def run_task2():
    extract("clothing.csv")

if __name__=="__main__":
    run_task2()

