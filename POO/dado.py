#Crea una clase "Dado" que simule el funcionamiento de un dado con caras del 1 al 6
#que tienen la misma probabilidad de salir y un programa de prueba.

import random
CARAS = 6

class Dado:
    def __init__(self):
        self.__valor = 1

    def lanzar(self):
        """Se lanza el dado y da un numero del 1 al 6"""
        self.__valor = random.randint(1, CARAS)

    @property
    def valor(self):
        return self.__valor

    def __str__(self):
        return f"El dado tiene {CARAS} caras y el valor es {self.__valor}"