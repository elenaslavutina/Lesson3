'''
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
 В каждом из классов реализовать переопределение метода draw.
 Для каждого из классов методы должен выводить уникальное сообщение.
  Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

'''
class Stationery:
    st_type = "неизвестный предмет"
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Я рисую {self.st_type} с названием {self.title}")

class Pen(Stationery):
    st_type = "Ручка"
    def draw(self):
        print(f"Я рисую {self.st_type}  с названием {self.title}")

class Pencil(Stationery):
    st_type  = "Карандаш"
    def draw(self):
        print(f"Я рисую {self.st_type}  с названием {self.title}")


class Handle(Stationery):
    st_type = "Маркер"

    def draw(self):
        print(f"Я рисую {self.st_type}  с названием {self.title}")

thing1 = Stationery("Staff")
thing2 = Pen("Stabio")
thing3 = Pencil("Kohinor")
thing4 = Handle("Erick")
thing1.draw()
thing2.draw()
thing3.draw()
thing4.draw()




