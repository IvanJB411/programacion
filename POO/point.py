#Implementa una clase Point con sus atributos x e y. La clase debe contener:
#su constructor, los getters y setters (propiedades),
#un invert_coordinates() que invierta las coordenadas x e y del punto.
#Además la clase debe tener un __str__() para poder imprimir los puntos en formato “(x,y)”.
#Implementa un test donde crees un punto,
#lo imprimas utilizando de manera implícita el método __str__(), imprimas su coordenada x,
#asignes 0 a su coordenada x, y vuelvas a imprimir el punto.


class Point:
    def __init__(self, x, y):
        self.__valor_x = x
        self.__valor_y = y

    @property
    def valor_x(self):
        return self.__valor_x
    @valor_x.setter
    def valor_x(self, value):
        self.__valor_x = value

    @property
    def valor_y(self):
        return self.__valor_y
    @valor_y.setter
    def valor_y(self, value):
        self.__valor_y = value

    def invertir_coordenadas(self):
        c = self.__valor_y
        self.__valor_y = self.__valor_x
        self.__valor_x = c
        """self.__x, self.__y = self.__y, self.__x"""
        return f"Las coordenadas quedarian, x= {self.__valor_x} e y= {self.__valor_y}"

    def __add__(self, other):
        return Point(self.__valor_x + other.__valor_x, self.__valor_y + other.__valor_y)

    def __sub__(self, other):
        return Point(abs(self.__valor_x - other.__valor_x), abs(self.__valor_y - other.__valor_y))

    def __str__(self):
        return f"({self.__valor_x}, {self.__valor_y})"

