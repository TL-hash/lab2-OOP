class Ship:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    def sail(self):
        print("{} has sailed!".format(self.name))

    def convert_cargo(self):
        cargo_kg = self.cargo * 1000
        return cargo_kg


def sail_function(name):
    print("{} has sailed!".format(name))

# #создание экземпляра класса Ship и вызов метода sail
black_pearl = Ship("Black Pearl", 800)
black_pearl.sail()

#вызов функции sail_function
sail_function(black_pearl.name)

print(black_pearl.convert_cargo())
