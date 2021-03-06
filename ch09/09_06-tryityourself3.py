from string import capwords

class Restaurant():
    # 3 arguments, self, r_n, and c_t
    def __init__(self, restaurant_name, cuisine_type):
        """ Create a restaurant with a name and food type."""
        # Each instance types restaurant name = the argument we give to restaurant
        # name. Same for cuisine_type.
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    # each instance gets this method available to it. the method prints both args
    # in a sentence. The self tells all characteristics associated with self (the class)
    # are available to it. 
    def describe_restaurant(self):
        print("Welcome to " + capwords(self.restaurant_name) + " where we make " +
                self.cuisine_type + " food and served " + str(self.number_served) + " people.")

    # Each instance also gets this method. It only uses the r_n arg. 
    def open_restaurant(self):
        print(capwords(self.restaurant_name) + " is now open!")

    def set_number_served(self, set_served):
        self.number_served += set_served

    def increment_number_served(self, more_served):
        self.number_served += more_served

# This is a subclass of restaurant, it imports Restaurant and customizes it.
# we can make a restaurant and have flavors. 
class IceCreamStand(Restaurant):
    """Represents an Ice Cream Stand Restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'honey']

    def flavor_list(self):
        print(self.flavors)

# Call class with required arguements
bobs = IceCreamStand('bob\'s', 'ice cream')
# Listt flavors which we defined as defaults in the subclass.
bobs.flavor_list() 



# Primary class here .It has some arguments assigned to it at run time and login_attempts
# at 0.
class User():
    def __init__(self, first_name, last_name, zip, age):
        """ Create a user an accept f & l name, zip, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.zip = zip
        self.age = age
        self.login_attempts = 0

# describe fucntion that stringifies and prints stuff. 
    def describe_user(self):
        print("You are " + self.first_name.title() + " " + self.last_name.title() +
                " and you are " + str(self.age) + " years old and live in " + 
                str(self.zip) + " zip code.")

# Add to login attempts one by one. 
    def increment_login_attempts(self):
        self.login_attempts += 1

# reset login_attempts to 0.    
    def reset_login_attempts(self):
        self.login_attempts = 0


# Subclass of User. All we do is call privileges class. 
class Admin(User):
    """This is a special user with special rights."""
    def __init__(self, first_name, last_name, zip, age):
        """Initialize attributes of the parent class."""
        super().__init__(first_name, last_name, zip, age)
        self.privs = Privileges()

# we assign some privs to the default class. show_privs just prints them.
class Privileges():
    """This is a special user with special rights."""
    def __init__(self):
        """Initialize attributes of the parent class."""
        self.privs = ['read', 'write', 'delete']

    def show_privs(self):
        print(self.privs) 


bob = Admin('bob', 'bobberson', '11111', 99)
bob.privs.show_privs()




class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has a " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject change if it tries to roll it back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles + self.odometer_reading >= self.odometer_reading:
            self.odometer_reading += miles
        else:
            print("You can't roll back the mileage!")

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Inititalize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describingg the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
