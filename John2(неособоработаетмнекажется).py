import random
import time
from typing import Dict


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.day = []
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.food = 5
        self.mess = 10
        self.job = job
        self.home = home
        self.car = car

    def get_job(self):
        job = get_work()
        self.job = job
        print(f"{self.name} got a new job as a {job.title}.")
        self.money += job.salary

    def get_home(self):
        self.home = House()
        print(f"{self.name} bought a new house.")

    def get_car(self):
        self.car = Auto(brands_of_car)
        print(f"{self.name} bought a new car.")

    def eat(self):
        if self.satiety <= 30:
            self.satiety += 40
            self.money -= 20
            print(f"{self.name} had a meal and gained 40 satiety points.")
        else:
            print(f"{self.name} is already full.")

    def work(self):
        if self.job is not None:
            if self.satiety >= 50:
                self.money += 100
                self.satiety -= 20
                self.gladness -= 10
                print(f"{self.name} worked hard and earned 100 money.")
            else:
                print(f"{self.name} is too hungry to work.")
        else:
            print(f"{self.name} has no job.")

    def shopping(self):
        if self.money >= 50:
            self.food += 10
            self.mess += 20
            self.money -= 50
            print(f"{self.name} went shopping and bought 10 food and 20 mess.")
        else:
            print(f"{self.name} doesn't have enough money to go shopping.")

    def chill(self):
        if self.gladness <= 40:
            self.gladness += 30
            self.satiety -= 10
            print(f"{self.name} had fun and gained 30 gladness points.")
        else:
            print(f"{self.name} doesn't feel like chilling.")

    def clean_home(self):
        if self.home is None:
            self.gladness -= 5
            print("You don't have a home")
        else:
            self.home.mess -= 10
            self.gladness -= 5
            print("You cleaned your home!")

    # def to_repair(self):
    #     if self.car is not None:
    #         self.car.strength = 100
    #         self.money -= 50
    #         print(f"{self.name} repaired the car.")
    #     else:
    #         print(f"{self.name} has no car.")

    def to_repair(self):
        if self.car is None:
            print("You don't have a car")
        else:
            repair_cost = 20
            if self.money < repair_cost:
                print("You don't have enough money to repair your car")
            else:
                self.money -= repair_cost
                self.car.strength = self.car.max_strength
                self.home.mess += 5
                print("You repaired your car!")

    def days_indexes(self, day):
        if not self.is_alive:
            return

        if self.home is None:
            self.get_home()

        if self.car is None:
            self.get_car()

        self.home.mess += 50
        indexes = [i for i in range(len(self.day)) if self.day[i] == day]

        if day % 7 == 0:
            self.money += 200
            print(f"{self.name} received a weekly salary of 200 money.")
        if day % 30 == 0:
            self.home.mess += 50
            print(f"{self.name}'s house got messier.")
        if day % 90 == 0:
            self.car.strength -= 20
            print(f"{self.name}'s car got weaker.")

    def buy_food(self):
        if self.money >= 10:
            self.money -= 10
            self.home.food += 1
            return True
        else:
            print(f"{self.name} does not have enough money to buy food.")
            return False

    # def eat(self):
    #     if self.home.food > 0:
    #         self.home.food -= 1
    #         return True
    #     else:
    #         print(f"{self.name} has no food to eat.")
    #         return False

    def buy_auto_fuel(self):
        if self.money >= 5:
            self.money -= 5
            self.car.fuel += 1
            return True
        else:
            print(f"{self.name} does not have enough money to buy fuel.")
            return False

    def drive_auto(self):
        if self.car.drive():
            print(f"{self.name} is driving the {self.car.brand}.")
        else:
            print(f"{self.name} cannot drive the {self.car.brand}.")

    def is_alive(self):
        if self.satiety <= 0:
            print('\033[91m' + f"{self.name} died of hunger." + '\033[0m')
            return False
        elif self.gladness <= 0:
            print('\033[91m' + f"{self.name} suicided." + '\033[0m')
            return False
        elif self.car is not None and self.car.strength <= 0:
            print('\033[91m' + f"{self.name} got no car." + '\033[0m')
            return False
        else:
            print('\033[92m' + f"{self.name} is still alive!" + '\033[0m')
            return True


brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6, "max_str": 100},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10, "max_str": 40},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8, "max_str": 150},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14, "max_str": 120},
}


def get_work():
    jobs = [
        Job("Developer", 500),
        Job("Accountant", 300),
        Job("Lawyer", 700),
        Job("Teacher", 200)
    ]

    print("Available jobs:")
    for i, job in enumerate(jobs):
        print(f"{i + 1}. {job.title} ({job.salary} per day)")

    choice = input("Enter job number: ")
    job = jobs[int(choice) - 1]

    return job


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]
        self.max_strength = brand_list[self.brand]["max_str"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("Car cannot move.")
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0





class Job:
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary


person = Human(name="John")

for day in range(1, 366):
    print(f"\nDay {day}")
    person.days_indexes(day)

    if person.is_alive():
        action = random.choice(["work", "eat", "chill", "clean_home", "shopping", "to_repair"])
        print(f"{person.name} decided to {action}.")
        if action == "work":
            person.work()
        elif action == "eat":
            person.eat()
        elif action == "chill":
            person.chill()
        elif action == "clean_home":
            person.clean_home()
        elif action == "shopping":
            person.shopping()
        elif action == "to_repair":
            person.to_repair()

        if day < 365 and not person.is_alive():
            break
    time.sleep(1)
