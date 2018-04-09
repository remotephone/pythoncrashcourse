# from module import class.
from modcar import Car

# define instance of class by following required arguments of the class
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# modify the instance with a function. 
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
