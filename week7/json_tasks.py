# Activity 1: Reading a JSON File
import json


def read(path):
    with open(path) as file:
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

#####################################
# Activity 2: Exporting to a JSON file


def read_task2(path):
    print("Reading...", end="")
    with open(path) as file:
        data = json.load(file)
    print("Done!")
    return data


def save(path, data):
    print("Exporting...", end="")
    with open(path, "w") as file:
        json.dump(data, file, indent = 4)
    print("Done!")


def run_task2():
    json_data = read_task2("futurama.json")
    save("exported.json", json_data)

run_task2()