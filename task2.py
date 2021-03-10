from abc import ABC, abstractmethod
class Dress(ABC):
  @staticmethod
  def common_expense(list_of_clothers):
    return sum(elem.expense for elem in list_of_clothers)

  @abstractmethod
  def expense(self):
    pass

  def __add__(self,other):
    return self.expense + other.expanse


class Suite(Dress):
    def __init__(self, size):
      self.size = size

    @property
    def expense(self):
        print(f"Затраты ткани на костюм - {round(2 * self.size + 0.3)}")
        return round(2 * self.size) + 0.3


class Coat(Dress):
    def __init__(self, height):
        self.height = height
    @property
    def expense(self):
        print(f"Затраты ткани на пальто - {round(self.height/6,5) + 0.5}")
        return round(self.height/6,5) + 0.5


s1 = Suite(44)
s2 = Suite(46)
c1 = Coat(17)
c2 = Coat(18)
list_cloth = [s1,s2,c1,c2]
print(Dress.common_expense(list_cloth))
