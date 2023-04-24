
import random


class Live:

    def __init__(self,name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        print(f'{self.name}')

    def to_study(self):
        print("Studying")
        self.gladness -= 3
        self.progress += 0.12

    def to_chill(self):
        print("Chilling")
        self.gladness += 5
        self.progress -= 0.1
    def to_sleep(self):
        print("Sleeping")
        self.gladness += 3


    def is_Alive(self):
        if self.progress <- 0.5:
            print("Cast out")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally")
            self.alive = False

    def end_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress,2)}")




    def live(self, day):
        day =  "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:^50}")
        live_cube = random.randint(1,3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_chill()
        elif live_cube == 3:
            self.to_sleep()

        self.end_day()
        self.is_Alive()


Gregory = Live(name='Gregory')

for day in range(365):
    if Gregory.alive == False:
        break
    Gregory.live(day)
