class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if value < 0:
            raise ValueError("Количество страниц не может быть отрицательным.")
        self._pages = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.author}"

    def __repr__(self):
        return f"PaperBook(name='{self.name}', author='{self.author}', pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if value < 0:
            raise ValueError("Продолжительность не может быть отрицательной.")
        self._duration = value

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"AudioBook(name='{self.name}', author='{self.author}', duration={self.pages})"
