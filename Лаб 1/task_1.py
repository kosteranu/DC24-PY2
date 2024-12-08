# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Dog:
    def __init__(self, breed: str, age: int, weight: float):
        """Создание и подготовка к работе объекта "Собака"

        :param breed: Порода собаки
        :param age: Возраст собаки в годах
        :param weight: Вес собаки в кг

        Примеры:
        >>> dog = Dog("Хаски", 3, 6.4) # инициализация экземпляра класса
        """
        if not isinstance(breed, str):
            raise TypeError("Порода должна быть типа str")
        self.breed = breed

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным числом")
        self.age = age

        if not isinstance(weight, float):
            raise TypeError("Вес должен быть типа float")
        if weight < 0:
            raise ValueError("Вес не может быть отрицательным числом")
        self.weight = weight

    def bark(self, duration: int) -> None:
        """Собака лает на протяжении задаваемого времени.
        :param duration: Время лая собаки в секундах

        :raise ValueError: Если время лая собаки - типа не int, то вызываем ошибку
        :raise ValueError: Если время лая собаки - отрицательное число, то вызываем ошибку

        Примеры:
        >>> dog = Dog("Хаски", 3, 6.4)
        >>> dog.bark(20)
        """
        pass

    def sit(self, duration: int) -> None:
        """Собака сидит на протяжении задаваемого времени.
        :param duration: Время сидения собаки в секундах

        :raise ValueError: Если время сидения собаки - типа не int, то вызываем ошибку
        :raise ValueError: Если время сидения собаки - отрицательное число, то вызываем ошибку

        Примеры:
        >>> dog = Dog("Хаски", 3, 6.4)
        >>> dog.sit(30)
        """
        pass

    def fetch_stick(self) -> bool:
        """Собака приносит палку.

        :return: Справилась ли собака

        Примеры:
        >>> dog = Dog("Хаски", 3, 6.4)
        >>> dog.fetch_stick()
        """
        pass


class Watch:
    def __init__(self, brand: str, _type: str, material: str):
        """Создание и подготовка к работе объекта "Часы"

        :param brand: Марка часов
        :param _type: Тип часов (например, наручные, настенные)
        :param material: Материал корпуса часов

        Примеры:
        >>> watch = Watch("Casio", "наручные", "металл") # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Марка должна быть типа str")
        self.brand = brand

        if not isinstance(_type, str):
            raise TypeError("Тип должен быть типа str")
        self._type = _type

        if not isinstance(material, str):
            raise TypeError("Материал должен быть типа str")
        self.material = material

    def show_time(self, timezone: str) -> str:
        """Часы показывают время в заданной временной зоне.
        :param timezone: Временная зона (например, "UTC+3")

        :raise ValueError: Если временная зона не str, то вызываем ошибку

        Примеры:
        >>> watch = Watch("Casio", "наручные", "металл")
        >>> watch.show_time("UTC+3")
        """
        pass

    def set_alarm(self, time: str) -> None:
        """Установка будильника на заданное время.
        :param time: Время будильника в формате "HH:MM"

        :raise ValueError: Если время будильника не str, то вызываем ошибку
        :raise ValueError: Если формат времени некорректный, то вызываем ошибку

        Примеры:
        >>> watch = Watch("Casio", "наручные", "металл")
        >>> watch.set_alarm("07:00")
        """
        pass

    def start_timer(self, duration: int) -> None:
        """Запуск таймера на заданное время.
        :param duration: Время таймера в секундах

        :raise ValueError: Если время таймера не int, то вызываем ошибку
        :raise ValueError: Если время таймера отрицательное, то вызываем ошибку

        Примеры:
        >>> watch = Watch("Casio", "наручные", "металл")
        >>> watch.start_timer(3600)
        """
        pass


class Bicycle:
    def __init__(self, brand: str, _type: str, gear_count: int):
        """Создание и подготовка к работе объекта "Велосипед"

        :param brand: Марка велосипеда
        :param _type: Тип велосипеда (например, горный, городской)
        :param gear_count: Количество передач на велосипеде

        Примеры:
        >>> bike = Bicycle("Giant", "горный", 21) # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Марка должна быть типа str")
        self.brand = brand

        if not isinstance(_type, str):
            raise TypeError("Тип должен быть типа str")
        self._type = _type

        if not isinstance(gear_count, int):
            raise TypeError("Количество передач должно быть типа int")
        if gear_count <= 0:
            raise ValueError("Количество передач должно быть положительным числом")
        self.gear_count = gear_count

    def ride(self, distance: float) -> None:
        """Поездка на велосипеде на заданное расстояние.
        :param distance: Расстояние поездки в километрах

        :raise ValueError: Если расстояние не float, то вызываем ошибку
        :raise ValueError: Если расстояние отрицательное, то вызываем ошибку

        Примеры:
        >>> bike = Bicycle("Giant", "горный", 21)
        >>> bike.ride(10.5)
        """
        pass

    def change_gears(self, gear: int) -> None:
        """Смена передачи на велосипеде.
        :param gear: Новая передача

        :raise ValueError: Если передача не int, то вызываем ошибку
        :raise ValueError: Если передача выходит за пределы допустимого диапазона, то вызываем ошибку

        Примеры:
        >>> bike = Bicycle("Giant", "горный", 21)
        >>> bike.change_gears(3)
        """
        pass

    def stop(self) -> None:
        """Остановка велосипеда.

        Примеры:
        >>> bike = Bicycle("Giant", "горный", 21)
        >>> bike.stop()
        """
        pass


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
