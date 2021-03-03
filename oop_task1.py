
'''
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.

'''
import time
from random import randint

colors = ["red", "yellow", "green"]
signal_duration = [7, 2, 15]


class TrafficLight:

    def __init__(self):

        # полный цикл
        self.__cycle_duration = sum(signal_duration)
        #время начала работы светофора
        self.__color = colors[0]

        self.__is_on = False

    def switch_on(self):
        if self.__is_on:
            print("Светофор уже включен!")
            return
        self.__is_on = True
        self.start_time = time.time()


    def switch_off(self):
        if not self.__is_on:
            print("Светофор уже выключен!")
            return
        self.__is_on = False
        self.start_time = time.time()

    def running(self):
         if self.__is_on:
                     # находим положение внутри цикла
                 secs = (time.time() - self.start_time) % self.__cycle_duration

                 if secs <= signal_duration[0]:
                         self.__color = colors[0]
                 elif secs <= signal_duration[0] + signal_duration[1]:
                         self.__color = colors[1]
                 else:
                     self.__color = colors[2]
                 return self.__color
         else:
             print("Светофор не работает! Сначала подключите светофор.")
             return

    def info(self):
        print(f"Заведена ли машина - {self.__is_on}")
    #    print(f"Какой цвет светофора сейчс - {self.__is_on")

def main():
    tl = TrafficLight()
    iter = 5
    max_sleep = 15
    tl.switch_on()

    for i in range(0, iter):
        secs = randint(0, max_sleep)
        print(time.time()-tl.start_time)
        print(f"Ждем {secs} секунд и проверяем состояние светафора")
        time.sleep(secs)
        print("Текущий цвет:", tl.running())

def test_check1_trafficlight():
    tl = TrafficLight()

    tl.switch_on()

    secs = 5
    time.sleep(secs)

    current = tl.running()

    assert current == colors[0]


def test_check2_trafficlight():
    tl = TrafficLight()

    tl.switch_on()

    secs = 8
    time.sleep(secs)

    current = tl.running()

    assert current == colors[1]


def test_check3_trafficlight():
    tl = TrafficLight()

    tl.switch_on()

    secs = 10
    time.sleep(secs)

    current = tl.running()

    assert current == colors[2]

main()
