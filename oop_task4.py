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
       #self.state = car_states[0]
    def speed_increace(self, ):

    def go(self, speed):
        if speed == 0:
            print("Вы стоите. Чтобы поехать нажмите на газ")
            return

        self.state = car_states[1]

    def stop(self):
        self.state = car_states[0]

    def stop(self, TurnRight = True):
        if TurnRight:
            self.state = car_states[2]
        else:
            self.state = car_states[3]

    def show_speed(self):
        return self.state


# Доделывай сама TownCar, SportCar, WorkCar, PoliceCar.
