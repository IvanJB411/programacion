#Crear la pila o cola
#Con o sin valores iniciales o a partir de otra pila o cola
#Obtener elementos
#Saber si esta vacia
#Vaciar

from xmlrpc.client import Boolean


class Pila:
    def __init__(self,*valores, otro=None):
        if otro is not None and isinstance(otro,Pila):
            self.__valores = otro.__valores.copy()
        else:
            self.__valores = list(valores)

    @property
    def valores(self):
        return self.__valores

    @valores.setter
    def valores(self,value):
        self.__valores = value

    @property
    def size(self):
        return len(self.__valores)

    @property
    def vacia(self):
        return not Boolean(self.size)

    def vaciar(self):
        self.__valores.clear()

    def push(self,value):
        self.__valores.insert(0,value)

    def pop(self):
        self.__valores.pop(0)

    def top(self):
        return self.__valores[0]

    def __str__(self):
        return f"{self.__valores}"

