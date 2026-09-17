class River:

    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        River.all_rivers.append(self)

    def get_info(self):
        print("Длина {0} равна {1} км".format(self.name, self.length))

volga = River("Volga", 10)
seine = River("Seine", 10)
nile = River("Nile", 10)

# for river in River.all_rivers:
#     print(river.name)

volga.get_info()
seine.get_info()
nile.get_info()
