from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()

        self.name = name
        self.power = power

    def run(self):

        print(f"{self.name}, на нас напали!")
        count_vrag = 100
        count_days = 0
        while count_vrag > 0:
            count_vrag = count_vrag - self.power
            count_days += 1
            time.sleep(1)
            print(f"{self.name} сражается {count_days}..., осталось {count_vrag} воинов.")
        print(f"{self.name} одержал победу спустя {count_days} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
time.sleep(1)
second_knight.start()
second_knight.join()
first_knight.join()







