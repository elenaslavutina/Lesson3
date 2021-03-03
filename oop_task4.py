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




class Car:
    auto_type = "General"
    fine = False

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0
        self.is_police = False
        self.max_speed = 180


    def speed_increace(self, interval ):
        if self.speed <= self.max_speed:
            self.speed = self.speed + interval
            print(f"Скорость автомобиля увеличена на {interval} км")
        else:
            print(f"Невозможно увеличить скорость на {interval}. Текущая скорость {self.speed}, а предельная {self.max_speed}")

    def speed_decreace(self, interval ):
        if self.speed >= interval:
            self.speed = self.speed - interval
            print(f"Скорость автомобиля уменьшена на {interval} км")
        else:
            print(f"Невозможно уменьшить скорость на {interval}. Текущая Скорость {self.speed}")

    def go(self, speed):
        if speed == 0:
            print("Вы стоите. Чтобы поехать увеличьте скорость")
            return

        self.speed = speed
        print(f"Автомобиль едет со скоростью {self.speed}")

    def stop(self):
        print("Вы остановились")
        self.speed = 0

    def show_speed(self):
        print(f"Ваша текущая скорость {self.speed}")
        return self.speed


    def fine_check(self):
        if self.fine:
            print(f"Автомобиль {self.name } У вас есть штраф!")
            return self.name
        else:
            print("Вы аккуратный водитель!")
            return


class TownCar(Car):
    auto_type = "TownCar"
    def show_speed(self):
        if self.speed > 60:
            self.fine = True
            print(f"Вы нарушаете скоростной режим. Разрешенная скорость 60 км.ч Ваша скорость {self.speed}")
        else:
            print(f"Ваша текущая скорость {self.speed}")
            return self.speed

class SportCar(Car):
    auto_type = "SportCar"
    def __init__(self, name, color):
        super().__init__(name,color)
        self.max_speed = 300



class WorkCar(Car):
    auto_type = "WorkCar"
    def __init__(self, name, color):
        super().__init__(name,color)
        self.max_speed = 100

    def show_speed(self):
        if self.speed > 40:
            self.fine = True
            print(f"Вы нарушаете скоростной режим. Выписан штраф.Разрешенная скорость 40 км.ч Ваша скорость {self.speed}")
        else:
            print(f"Ваша текущая скорость {self.speed}")
            return self.speed



class PoliceCar(Car):
    auto_type = "PoliceCar"

    def __init__(self, name, color ):
        super().__init__(name,color)
        self.is_police = True

Auto1 = Car("Kia","black")
Auto2 = SportCar("Mazerati", "red")
Auto3 = TownCar ("Folwvagen","Broun")
Auto4 = WorkCar("Kamaz","grey")
Auto5 = PoliceCar("Lada", "white/blue")
print(f"Первая машина {Auto1.auto_type}, {Auto1.name}, {Auto1.color} ")
print(f"Вторая машина {Auto2.auto_type},{Auto2.name}, {Auto2.color}")
print(f"Третья машина {Auto3.auto_type},{Auto3.name}, {Auto3.color}")
print(f"Четвертая машина {Auto4.auto_type},{Auto4.name}, {Auto4.color}")
print(f"Пятая машина {Auto5.auto_type},{Auto5.name}, {Auto5.color}")
Auto1.show_speed()
Auto1.speed_increace(20)
Auto1.show_speed()
Auto2.show_speed()
Auto2.go(200)
Auto4.go(80)
Auto4.show_speed()
Auto4.fine_check()

