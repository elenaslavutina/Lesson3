'''
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.

При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''


car_states = ["Stop", "Go", "TurnRight", "TurnLeft"]

class Car:

    def __init__(self, name, color, speed = 0, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        self.max_speed = 180
       #self.state = car_states[0]

    def speed_increace(self, interval ):
        if self.speed <= self.max_speed:
            self.speed = self.speed + interval
        else:
            print(f"Невозможно увеличить скорость на {interval}. Текущая скорость {self.speed}, а предельная {self.max_speed}")

    def speed_decreace(self, interval ):
        if self.speed >= interval:
            self.speed = self.speed - interval
        else:
            print(f"Невозможно уменьшить скорость на {interval}. Текущая Скорость {self.speed}")

    def go(self, speed):
        if speed == 0:
            print("Вы стоите. Чтобы поехать увеличте скорость")
            return

        self.state = car_states[1]

    def stop(self):
        self.speed = 0



    def show_speed(self):
        return self.speed

