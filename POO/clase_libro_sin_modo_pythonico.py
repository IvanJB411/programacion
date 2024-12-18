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


    def get_isbn(self):
        return self.__isbn



    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_number_pages(self):
        return self.__number_pages

    def set_number_pages(self, number_pages):
        self.__number_pages = number_pages



# test
libro = Book("548fk", "juan")
libro.get_isbn()
libro.set_number_pages(300)
libro.set_title("Hola")
print(f"El libro con titulo {libro.get_title()} con isbn {libro.get_isbn()} y su autor es {libro.get_author()}")