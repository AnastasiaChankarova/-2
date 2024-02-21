class Animal:
    def __init__(self, name: str, age: int, color: str):
        """
        Конструктор для класса Animal.

        Args:
        name (str): имя животного..
        age (int): возраст животного.
        color (str): цвет животного.
        """
        self._name = name
        self._age = age
        self._color = color

    def make_sound(self) -> str:
        """
        Животное издает звуки.

        Returns:
        str: звуки животного.
        """
        pass

    def move(self) -> str:
        """
        Животное движется.

        Returns:
        str: движение животного.
        """
        pass

    def __str__(self) -> str:
        """
        Представление животного.

        Returns:
        str: представление животного.
        """
        pass

    def __repr__(self) -> str:
        """
        Изображение животного.

        Returns:
        str: изображение животного.
        """
        pass

class Dog(Animal):
    def __init__(self, name: str, age: int, color: str, breed: str):
        """
        Конструктор для класса Dog

        Args:
        name (str): кличка собаки.
        age (int): возраст собаки.
        color (str): окрас собаки.
        breed (str): порода собаки.
        """
        super().__init__(name, age, color)
        self._breed = breed

    def make_sound(self) -> str:
        """
        Звуки, похожие на собачий лай.

        Returns:
        str: Звуки лая собаки.
        """
        return "Гав-гав!"

    def move(self) -> str:
        """
        Движения собаки.

        Returns:
        str: Движение собаки.
        """
        return "Бежит и виляет хвостом"

    def __str__(self) -> str:
        """
        Неформальное представление собаки.

        Returns:
        str: неформальное представление собаки.
        """
        return f"A {self._color} {self._breed} dog named {self._name}"

    def __repr__(self) -> str:
        """
        Официальное представление собаки.

        Returns:
        str: Официальное представление собаки.
        """
        return f"Dog(name='{self._name}', age={self._age}, color='{self._color}', breed='{self._breed}')"

class Cat(Animal):
    def __init__(self, name: str, age: int, color: str, breed: str):
        """
        Конструктор для класса Cat

        Args:
        name (str): кличка кошки.
        age (int): возраст кошки.
        color (str): цвет кошки.
        breed (str): порода кошки.
        """
        super().__init__(name, age, color)
        self._breed = breed

    def make_sound(self) -> str:
        """
        Звуки, похожие на кошку.

        Returns:
        str: Мяуканье кошки.
        """
        return "Мяу!"

    def move(self) -> str:
        """
        Движения кошки.

        Returns:
        str: движения кошки.
        """
        return "Крадется и мурлычет"

    def __str__(self) -> str:
        """
        Неформальное представление кошки.

        Returns:
        str: Неформальное представление кошки.
        """
        return f"A {self._color} {self._breed} cat named {self._name}"

    def __repr__(self) -> str:
        """
        Официальное представление кошки.

        Returns:
        str: Официальное представление кошки.
        """
        return f"Cat(name='{self._name}', age={self._age}, color='{self._color}', breed='{self._breed}')"
    ...

if __name__ == "__main__":
    # Write your solution here
    pass