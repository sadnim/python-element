from driver import Driver
from engine import Engine

class Car:
    car_name: str
    car_class: str
    car_weight: float
    driver: Driver
    engine: Engine

    def start():
        print("Let's go")

    def stop():
        print("Slowing down")

    def turnLeft():
        print("Turning left")

    def turnRight():
        print("Turning right")

    def toString(self):
        print(self.car_name, self.car_weight, self.car_class, self.driver, self.engine)

class Lorry(Car):
    load_capacity: int

    def __init__(self, name, category, weight, load_capacity):
        self.car_name = name
        self.car_class = category
        self.car_weight = weight
        self.load_capacity = load_capacity

class SportCar(Car):
    max_speed: int

    def __init__(self, name, category, weight, max_speed):
        self.car_name = name
        self.car_class = category
        self.car_weight = weight
        self.max_speed = max_speed