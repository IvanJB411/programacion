#Implementa la clase Rectangulo (determinado por dos objetos Point) que además de su constructor,
# tendrá dos métodos para calcular su área y su perímetro que tienes que transformar en propiedades.
# Implementa también un test que cree dos puntos y un rectángulo a partir de estos dos puntos y que muestre el área y perímetro de dicho rectángulo

class Rectangulo:
    def __init__(self, p1, p2):
        self.__punto1 = p1
        self.__punto2 = p2

    @property
    def punto1(self):
        return self.__punto1

    @punto1.setter
    def punto1(self, value):
        self.__punto1 = value

    @property
    def punto2(self):
        return self.__punto2
    @punto2.setter
    def punto2(self, value):
        self.__punto2 = value

    @property
    def area(self):
        return abs(self.__punto2.valor_x - self.__punto1.valor_x) * abs(self.__punto2.valor_y - self.__punto1.valor_y)

    @property
    def perimetro(self):
        return 2 * (abs(self.__punto2.valor_x - self.__punto1.valor_x) + abs(self.__punto2.valor_y - self.__punto1.valor_y))

    def __str__(self):
        return f"El rectangulo tiene un punto {self.__punto1} y otro punto {self.__punto2}. Su area es {self.area} y el perimetro {self.perimetro}"