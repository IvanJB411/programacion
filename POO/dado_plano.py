#Implementar otra clase Dado. Por defecto el dado tendrá 6 caras.
#Tendremos tres formar de construir un dado (uno al que no se le pasa nada e inicializa el dado al azar,
#otro al que sólo se le pasa que número tiene el dado en la cara superior y
#otro con el número del dado en la cara superior y el número de caras del dado).
#Implementa los getters, el método roll() que tirará el dado al azar y el __str__().
#Implementa un tester que tenga un vector de 4 dados y los lance una serie de veces.
# Dado solo / Dado con valor / Dado con valor y caras

import random

NUM_CARAS = 6

class DadoSimple:
    def __init__(self, caras=NUM_CARAS, valor=1):
        self.__caras = caras
        self.__valor = valor

    def roll(self):
        self.__valor = random.randint(1,self.caras)

    @property
    def caras(self):
        return self.__caras

    @property
    def valor(self):
        return self.__valor

    def __str__(self):
        return f"El dado tiene {self.caras} caras y su valor es {self.__valor}"
