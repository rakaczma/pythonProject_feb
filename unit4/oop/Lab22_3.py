class Book:

    def __init__(self, title, author, publisher, year):
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__year = year

    def show_short_info(self):
        print("tytuł:", self.__title, "autor", self.__author)

    def show_full_info(self):
        print("tytuł:", self.__title, "autor", self.__author, "wydawca", self.__publisher, "rok wydania", self.__year)

books = []
books.append((Book("Dzieci z Bulerbyn", "Astrid Lindgren", "nasza księgarnia", 2014)))
books.append((Book("Moby Dick", "Herman Marville", "nasza księgarnia", 2009)))
books.append((Book("Python. Wprowadzenie", "Mark Lutz", "nasza księgarnia", 2022)))

for b in books:
    b.show_short_info()