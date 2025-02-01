class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


# class PaperBook:
#     def __init__(self, name: str, author: str, pages: int):
#         self.name = name
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return f"Книга {self.name}. Автор {self.author}"


# class AudioBook:
#     def __init__(self, name: str, author: str, duration: float):
#         self.name = name
#         self.author = author
#         self.duration = duration
#
#     def __str__(self):
#         return f"Книга {self.name}. Автор {self.author}"


class PaperBook(Book):
    """ Наследованный класс бумажной книги от класса книги. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if type(pages) is int:
            self.pages = pages
        else:
            raise TypeError("Введите целочисленное значение")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ Наследованный класс аудиокниги от класса книги. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if type(duration) is float:
            self.duration = duration
        else:
            raise TypeError("Введите вещественное значение")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.duration!r})"


paper = PaperBook("1984", "Orwell", 300)
print(repr(paper))
audio = AudioBook("1984", "Orwell", 30.2)
print(repr(audio))
