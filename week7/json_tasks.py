# Activity 1: Reading a JSON File
import json

def read(path):
    with open("futurama.json") as file:
        data = json.load(file)
        location = data["location"]
        print(f"Place Name: {location}")
        population = data["population"]
        print(f"Population Size: {population}")
        bots = data["bots"]
        for bot in bots:
            name = bot["name"]
            stats = bot["stats"]
            print(f"{name} has strength level of {stats["strength"]} and speed level of {stats["speed"]}. ")

def run():
    read("futurama.json")

if __name__ == "__main__":
    run()