class Rectangle:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, w):
        self.__width = w

    def get_height(self):
        return self.__height

    def set_height(self, h):
        self.__height = h

    def area(self):
        return self.__width * self.__height

#с двумя подчеркиваниями нужно работать только через get_width()
rect = Rectangle(10, 20)
print(rect.get_width())

#атрибут теперь носит название _Rectangle__width
rect._Rectangle__width = 20
print(rect.get_width())
