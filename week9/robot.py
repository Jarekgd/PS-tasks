# Activity 1: Basic Class
class Robot:
    MAX_ENERGY = 100

    def __init__(self, name="Robot", age=0, energy=MAX_ENERGY):
        self.name = name
        self.age = age
        self.energy = 0

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f'robot(name={self.name}, age={self.age})'

    def __str__(self):
        return f'Robot {self.name} is {self.age} years old.'

    def grow(self):
        self.age += 1
        return self.age

    def eat(self, amount):
        if self.energy + amount < self.MAX_ENERGY:
            self.energy += amount
        else:
            self.energy = self.MAX_ENERGY
        return self.energy

    def move(self, distance):
        if self.energy - distance > 0:
            self.energy -= distance
        else:
            self.energy = 0
        return self.energy


if __name__ == "__main__":
    robot = Robot()
    robot.display()
    print(repr(robot))
    print(robot)
    print(robot.grow())
    robot.grow()
    print(f"One more time: {robot.grow()}")
    print(f"Eating grow: {robot.eat(10)}")
    print(f"Eating grow: {robot.eat(7)}")
    print(f"After move: {robot.move(40)}")
    print(f"Eating grow: {robot.eat(7)}")

