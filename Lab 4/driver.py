class Person():
    date_of_birth: str
    gender: bool

class Driver(Person):
    first_name: str #imya
    middle_name: str #otschestvo
    last_name: str #familiya
    experience: int
    car_category: str

    def __init__(self, first_name, middle_name, last_name, experience, category):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.experience = experience
        self.car_category = category
