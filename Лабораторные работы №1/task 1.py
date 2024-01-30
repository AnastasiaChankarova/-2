# TODO Написать 3 класса с документацией и аннотацией
# типов
import doctest
class Table:
    def __init__(self, material: str, sort: int):
        """
        Создание и подготовка к работе объекта "Стол"

        :param material: вид дерева
        :param sort: сорт древесины

        >>> table = Table("Сосна", 2)
        """
        if not isinstance(material, str):
            raise ValueError("Вид дерева должен быть типа 'str'")
        self.material = material

        if not isinstance(sort, int):
            raise ValueError("Сорт древесины должен быть типа 'int'")
        if sort < 0:
            raise ValueError("Сорт древесины не может быть отрицательным числом")
        self.sort = sort

    def paint(self, content: str) -> None:
        """
        Метод, позволяющий покрывать стол указанным цветом
        :param content: выбранный цвет
        >>> table = Table("Сосна", 2)
        >>> table.paint("Красный")
        """
        ...

    def size(self, content: str) -> None:
        """
        Метод, позволяющий указать габариты стола
        :param content: указанные габариты
        >>> table = Table("Сосна", 2)
        >>> table.size("120x80x40")
        """
        ...

class Car:
    def __init__(self, brand: str, speed_max: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"
        :param brand: марка автомобиля
        :param speed_max: макс скорость автомобиля

        >>> car = Car("BMW", 270)
        """
        if not isinstance(brand, str):
            raise ValueError("Марка автомобиля должна быть типа 'str'")
        self.brand = brand

        if not isinstance(speed_max, int):
            raise ValueError("Макс скорость автомобиля должен быть типа 'int'")
        if speed_max < 0:
            raise ValueError("Макс скорость автомобиля не может быть отрицательным числом")
        self.speed_max = speed_max

    def car_contrast(self, car_2) -> bool:
        """
        Метод, позволяющий сравнивать автомобили разных марок
        :param car_2: сравнение
        >>> car_1 = Car("BMW", 270)
        >>> car_2 = Car("Audi", 250)
        >>> car_1.car_contrast(car_2)
        """
        ...

    def car_info(self) -> bool:
        """
        Метод, позволяющий получить информацию об экстерьере автомобиля
        :param info: информация
        >>> car = Car("BMW", 270)
        >>> car.car_info()
        """
        ...

class Vk:
    def __init__(self, id: int, name: str):
        """
        Создание и подготовка к работе объекта "Вк"
        :param id: персональный номер пользователя
        :param name: имя пользователя
        >>> vk = Vk(5768832,"Юрий")
        """
        if not isinstance(id, int):
            raise ValueError("Персональный номер должен быть типа 'int'")
        if id < 0:
            raise ValueError("Персональный номер не может быть отрицательным числом")
        self.id = id

        if not isinstance(name, str):
            raise ValueError("Имя пользователя должно быть типа 'str'")
        self.name = name

    def create_post(self, content: str) -> bool:
        """
        Метод, позволяющий создать новый пост на странице пользователя.
        :param content: содержание поста
        >>> vk = Vk(5768832,"Юрий")
        >>> vk.create_post()
        """
        ...

    def send_friend_request(self, user_id: int) -> bool:
        """
        Метод, позволяющий отправить запрос на добавление пользователя в друзья.
        :param user_id: персональный номер пользователя
        >>> vk = Vk(5768832,"Юрий")
        >>> vk.send_friend_request()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
        # TODO работоспособность экземпляров класса проверить с помощью doctest

