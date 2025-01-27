# Classes 101 - Create a class car - Py_learn_projectn
class Car:
    vehicle = 'Automobile'
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
           return print(f"{self.year} {self.brand} { self.model}") 
    def is_old(self):
        return 2025 - self.year > 10 
##
myFirtCar,mySecondCar = Car('Toyota', 'Corolla', 2012), Car('BMW', 'X5', 2019)
print(type(myFirtCar))
myFirtCar.display_info()
print(myFirtCar.is_old())
mySecondCar.display_info()
if mySecondCar.is_old():
    print('This car is old')
else:
    timeLeft = 10 - (2025 - mySecondCar.year)  
    oldYear = 2025 + timeLeft
    print(f'This car is still new, after {timeLeft} years it will be considered old in the year {oldYear}')     