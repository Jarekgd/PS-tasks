class Human:
    MAX_ENERGY = 100

    def __init__(self, name="Human", age=0):
        self.name = name
        self.age = int(age)
        self.energy = Human.MAX_ENERGY

    def __repr__(self):
        return f'human(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self):
        return f'Human {self.name} is {self.age} years old.'

    def display(self):
        print(f"I am {self.name}")

    def grow(self):
        print(self.age + 1)

    def eat(self, amount):
        potential_energy = self.energy + amount
        if potential_energy > Human.MAX_ENERGY:
            self.energy = Human.MAX_ENERGY
            return potential_energy - self.energy
        else:
            self.energy = potential_energy
        return 0

    def move(self, distance):
        potential_energy = self.energy - distance
        if potential_energy < 0:
            self.energy = 0
            return self.energy - abs(potential_energy)
        else:
            self.energy = potential_energy
            return 0


if __name__ == "__main__":
    human = Human("Jarek", 58)
    print(human)
    print(repr(human))
    human.move(10)
    print(repr(human))
    human.eat(5)
    print(repr(human))
    human.eat(20)
    print(repr(human))
