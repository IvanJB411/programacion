"""Crea una clase para almacenar duraciones de tiempo (Duration). Los objetos de esta clase son intervalos de tiempo y se crean de la forma:
t1 = Duration(1, 20, 30)  # almacenará 1 hora, 20 minutos y 30 segundos.
t2 = Duration(2, 75, -10)  # almacenará 3 horas, 14 minutos y 50 segundos.
t3 = Duration(t2)  # almacenará las horas, minutos y segundos del objeto t2
Crea los getters y setters mediante propiedades y métodos para:
    Sumar y restar objetos de la clase sobrecargando operadores (el resultado es otro objeto).
    Sumar y restar segundos, minutos o horas (se cambia el objeto actual).
    Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10h 35m 5s."""

class Duration:
    def __init__(self, horas,minutos, segundos, otro=None):
        if otro is not None and isinstance(otro, Duration):
            self.__horas = otro.__horas
            self.__minutos = otro.__minutos
            self.__segundos = otro.__segundos
        else:
            self.__horas = horas
            self.__minutos = minutos
            self.__segundos = segundos

    @property
    def horas(self):
        return self.__horas

    @horas.setter
    def horas(self, value):
        self.__horas = value

    @property
    def minutos(self):
        return self.__minutos

    @minutos.setter
    def minutos(self, value):
        self.__minutos = value

    @property
    def segundos(self):
        return self.__segundos

    @segundos.setter
    def segundos(self, value):
        self.__segundos = value

    def __regularizar(self):
        segundos_totales = self.__horas * 3600 +self.__minutos * 60 + self.__segundos
        self.__horas = segundos_totales // 3600
        self.__minutos = (segundos_totales % 3600) // 60
        self.__segundos = (segundos_totales % 3600) % 60

    def sumar_segundos(self, value):
        self.__segundos += value
        self.__regularizar()

    def sumar_minutos(self, value):
        self.__minutos += value
        self.__regularizar()


    def sumar_horas(self, value):
        self.__horas += value
        self.__regularizar()


    def __str__(self):
        return f"{self.__horas}h {self.__minutos}m {self.__segundos}s"