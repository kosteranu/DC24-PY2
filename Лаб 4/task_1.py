if __name__ == "__main__":
    # Write your solution here
    class Car:
        """Базовый класс автомобиля
        :param color: цвет машины типа str
        :param max_speed: максимальная скорость в км/ч типа float больше 0
        :param tank_volume: объем топливного бака в литрах типа int не меньше 0
        """
        def __init__(self, color: str, max_speed: float, tank_volume: int):
            self.color = color
            if max_speed > 0 and tank_volume >= 0:
                self.max_speed = max_speed
                self.tank_volume = tank_volume
            else:
                raise ValueError("Не вводите отрицательные значения")

        def __str__(self):
            return f"Цвет {self.color}. Максимальная скорость {self.max_speed}"

        def __repr__(self):
            return f"{self.__class__.__name__}(color={self.color!r}, max_speed={self.max_speed!r}, tank_volume={self.tank_volume!r})"

        def start_engine(self) -> None:
            """Метод запускает двигатель машины"""
            print("Двигатель запущен")

        def refuel(self) -> None:
            """Заправляет бак, если он пуст, или сообщает, что он еще полон"""
            if self.tank_volume > 0:
                print("Топливный бак еще полный")
            else:
                print("Топливный бак заполнен")


    class Truck(Car):
        """Наследованный класс грузовика от автомобиля
        :param color: цвет машины типа str
        :param max_speed: максимальная скорость в км/ч типа float больше 0
        :param tank_volume: объем топливного бака в литрах типа int не меньше 0
        :param with_trailer: наличие трейлера или его отсутствие типа bool
        """
        def __init__(self, color: str, max_speed: float, tank_volume: int, with_trailer: bool):
            super().__init__(color, max_speed, tank_volume)
            self.with_trailer = with_trailer

        def __repr__(self):
            return f"{self.__class__.__name__}(color={self.color!r}, max_speed={self.max_speed!r}, tank_volume={self.tank_volume!r}, with_trailer={self.with_trailer})"

        def action_with_trailer(self) -> None:
            """Метод отсоединяет трейлер, если он присоединен, и присоединяет, если он отсоединен"""
            if self.with_trailer:
                print("Трейлер отсоединен")
            else:
                print("Трейлер присоединен")


    class Electric(Car):
        """Наследованный класс электромобиля от автомобиля
        :param color: цвет машины типа str
        :param max_speed: максимальная скорость в км/ч типа float больше 0
        :param bat_capacity: объем батареи в мАч типа int не меньше 0
        """
        def __init__(self, color: str, max_speed: float, bat_capacity: int):
            super().__init__(color, max_speed, bat_capacity)
            self.bat_capacity = bat_capacity

        def __repr__(self):
            return f"{self.__class__.__name__}(color={self.color!r}, max_speed={self.max_speed!r}, bat_capacity={self.bat_capacity!r})"

        def refuel(self) -> None:
            """Электромобиль имеет батарею, а не топливный бак"""
            if self.bat_capacity > 0:
                print("Батарея еще не разряжена")
            else:
                print("Батарея заряжена")

    pass

