class Book1:

    def __init__(self, isbn, title, author, pages):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__number_pages = pages
    @property
    def isbn(self):
        return self.__isbn

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value.upper()

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value.upper()

    @property
    def number_pages(self):
        return self.__number_pages

    @number_pages.setter
    def number_pages(self, value):
        self.__number_pages = value

    def __str__(self):
        #Imprimir El libro con titulo....
        return f"Metodo str: \n El libro con titulo {self.title} e isbn {self.isbn}, de {self.author}, tiene {self.number_pages} paginas"
    def __repr__(self):
        #Imprimir libro(....)
        return f"Metodo repr: \n Libro({self.isbn}, {self.title}, {self.author}, {self.number_pages})"
