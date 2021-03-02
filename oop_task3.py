'''
Реализовать базовый класс Worker (работник),
в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:

    def __init__(self, name, lastname, position, wage, bonus):
        self.name = name
        self.lastname = lastname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}


class Position(Worker):

  #  def __init__(self, name, lastname, position, wage, bonus):
   #     super().__init__(name, lastname, position, wage, bonus)

    def get_full_name(self):
        return self.name + " " + self.lastname

    def get_total_income(self):
        return self._Worker__income["wage"] + self._Worker__income["bonus"]


pos = Position("Иван", "Петров", "Директор", 100, 50)

print(pos.get_full_name(), pos.get_total_income())
