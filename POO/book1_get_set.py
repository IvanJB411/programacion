class Book1:

    def __init__(self, isbn, title, author):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__number_pages = 0

    def get_isbn(self):
        return  self.__isbn

    def get_title(self):
        return  self.__title
    def set_title(self, value):
        self.__title = value

    def get_author(self):
        return  self.__author
    def set_author(self, value):
        self.__author = value

    def get_number_pages(self):
        return  self.__number_pages
    def set_number_pages(self, value):
        self.__number_pages = value