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

# First instance of class. Define the instance, passing required arguments
my_new_car = Car('audi', 'a4', 2016)
# Print this instance's descriptive name.
print(my_new_car.get_descriptive_name())

# Update mileage by specifying a new value
# my_new_car.odometer_reading = 23

#Update using the update_odometer() function
my_new_car.update_odometer(23)
# Print value of odometer
my_new_car.read_odometer()

# New instance of Car. This is a used car, we need it to have more miles and add even more.
my_used_car = Car('subaru', 'outback', 2013)
# Print instances description.
print(my_used_car.get_descriptive_name())
# Assign 23.5k miles to reading now and print that reading.
my_used_car.update_odometer(23500)
my_used_car.read_odometer()

# Increase that by 100. 
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# Let's try to roll that back.

my_used_car.increment_odometer(-100)
my_used_car.read_odometer()