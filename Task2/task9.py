from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, year):
        self.title = title
        self.year = year

    @abstractmethod
    def info(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, author, year):
        super().__init__(title, year)
        self.author = author

    def info(self):
        return f"Книга: {self.title}, автор: {self.author}, рік: {self.year}"

class Magazine(LibraryItem):
    def __init__(self, title, issue, year):
        super().__init__(title, year)
        self.issue = issue

    def info(self):
        return f"Журнал: {self.title}, випуск: {self.issue}, рік: {self.year}"


class Reader:
    def __init__(self, name):
        self.name = name
        self.__borrowed_items = []  

    def borrow(self, item: LibraryItem):
        self.__borrowed_items.append(item)
        print(f"{self.name} взяв: {item.info()}")

    def show_borrowed(self):
        print(f"\n{self.name} взяв наступні предмети:")
        for item in self.__borrowed_items:
            print("-", item.info()) 