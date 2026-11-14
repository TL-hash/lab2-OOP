class Ship:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    def name_captain(self, cap):
        self.captain = cap
        print("{} is the captain of the {}".format(self.name, self.captain))

    def load_cargo(self, weight):
        if self.cargo + weight <= self.capacity: #if weight <= self.free.space()
            self.cargo += weight
            print("Loaded {} tons".format(weight))
        else:
            print("Cannot load that much")

    def unload_cargo(self, weight):
        if self.cargo - weight >= 0:
            self.cargo -= weight
            print("Unloaded {} tons".format(weight))
        else:
            print("Cannot unload that much")

    def free_space(self):
        return self.capacity - self.cargo

black_pearl = Ship("Black Pearl", 800)
#
# # # ошибка, так как атрибут captain создается только в методе name_captain
# # print(black_pearl.captain) #AttributeError
#
#
# black_pearl.name_captain("Jack Sparrow")
#
# print(black_pearl.captain)

#пример
black_pearl.load_cargo(600)
black_pearl.unload_cargo(400)
black_pearl.load_cargo(700)
black_pearl.unload_cargo(300)
