class Pet:

    kind = "mammal"
    n_pets = 0
    pet_names = []

    def __init__(self, spec, name):
        self.spec = spec
        self.name = name
        self.legs = 4

tom = Pet("cat", "Tom")
avocado = Pet("dog", "Avocado")
ben = Pet("goldfish", "Ben")

# #получим доступ к атрибуту класса напрямую через класс
# Pet.n_pets += 3
#
# print(Pet.n_pets)
# print(tom.n_pets)
# print(avocado.n_pets)
# print(ben.n_pets)

# #доступ к атрибуту класса через экземпляр
# tom.n_pets += 1
# avocado.n_pets += 1
# ben.n_pets += 1
#
# print(Pet.n_pets)
# print(tom.n_pets)
# print(avocado.n_pets)
# print(ben.n_pets)

# #изменение атрибута одного экземпляра не изменит их для всего класса
# ben.kind = "fish"
#
# print(Pet.kind)
# print(tom.kind)
# print(avocado.kind)
# print(ben.kind)

# #атрибут pet_names является изменяемым списком, поэтому изменения
# # влияют на весь класс
# tom.pet_names.append(tom.name)
# avocado.pet_names.append(avocado.name)
# ben.pet_names.append(ben.name)
#
# print(Pet.pet_names)
# print(tom.pet_names)
# print(avocado.pet_names)
# print(ben.pet_names)

# #создание нового списка для сохранения атрибутом класса pet_names
# # разных значений для разных экземпляров
# tom.pet_names = ["Tom"]
# avocado.pet_names = ["Avocado"]
# ben.pet_names = ["Ben"]
#
# print(Pet.pet_names)
# print(tom.pet_names)
# print(avocado.pet_names)
# print(ben.pet_names)

#добавление атрибутов
Pet.all_specs = [tom.spec, avocado.spec, ben.spec]

print(tom.all_specs)
print(avocado.all_specs)
print(ben.all_specs)
