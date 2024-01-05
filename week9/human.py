# Activity 1: Basic Class
class Human:
    MAX_ENERGY = 100

    def __init__(self, name="Human", age=0, energy=MAX_ENERGY):
        self.name = name
        self.age = age
        self.energy = energy

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f'human(name={self.name}, age={self.age})'

    def __str__(self):
        return f'Human {self.name} is {self.age} years old.'

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
    human = Human()
    human.display()
    print(repr(human))
    print(human)
    print(human.grow())
    human.grow()
    print(f"One more time: {human.grow()}")
    print(f"Eating grow: {human.eat(10)}")
    print(f"Eating grow: {human.eat(7)}")
    print(f"After move: {human.move(40)}")
    print(f"Eating grow: {human.eat(7)}")
