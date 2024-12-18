"""
Definición de la clase Libro con los atributos isbn, autor, título y número de páginas.

Ejemplo sacado del libro "Aprende Java con Ejercicios" de Luis José Sánchez:
https://github.com/LuisJoseSanchez/aprende-java-con-ejercicios

Adaptado a Python por Rafael del Castillo Gomariz.

Fecha: 7/01/2023.
"""

class Book:

    def __init__(self, isbn, author):
        """
        Método constructor que es llamado cada que se instancie un objeto de esta clase.
        En este ejemplo solo crearemos los atributos (públicos). Anteponer 'self' es necesario para indicar que estos
        pertenecen al objeto instanciado.
        """
        self.__isbn = isbn
        self.__title = ''
        self.__author = author
        self.__number_pages = 0

    @property
    def isbn(self):
        return self.__isbn

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def number_pages(self):
        return self.__number_pages


    @title.setter
    def title(self, value):
        self.__title = value

    @author.setter
    def author(self, value):
        self.__author = value

    @number_pages.setter
    def number_pages(self, value):
        self.__number_pages = value

# test
libro = Book("548fk", "juan")
libro.number_pages = 300
libro.title = "Titulo del libro"

print(f"El libro con titulo {libro.title} con isbn {libro.isbn} y su autor es {libro.author}")