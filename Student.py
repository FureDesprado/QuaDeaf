import random

class Live:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 1000
        self.alive = True
        self.days_since_last_payment = 0
        print(f'{self.name}')

    def to_study(self):
        print("Studying")
        self.gladness -= 3
        self.progress += 0.12

    def to_chill(self):
        print("Chilling")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 50

    def to_sleep(self):
        print("Sleeping")
        self.gladness += 3

    def to_work(self):
        print("Working")
        self.gladness -= 2
        self.progress += 0.08
        self.money += 100

    def make_payment(self):
        print("Paying tuition")
        self.money -= 500
        self.days_since_last_payment = 0

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally")
            self.alive = False
        elif self.money <= 0:
            print("Broke")
            self.alive = False

    def end_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")
        print()

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_chill()
        elif live_cube == 3:
            self.to_sleep()
        else:
            self.to_work()

        self.days_since_last_payment += 1
        if self.days_since_last_payment == 30:
            self.make_payment()

        self.end_day()
        self.is_alive()

        if self.alive and self.money <= 0:
            print("You are out of money. Randomly choose what to do:")
            choice = random.randint(1, 2)
            if choice == 1:
                print("Going to work")
                self.to_work()
            elif choice == 2:
                print("Going to study")
                self.to_study()

Gregory = Live(name='Gregory')

for day in range(365):
    if not Gregory.alive:
        break
    Gregory.live(day)
