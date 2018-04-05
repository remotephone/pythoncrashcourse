from string import capwords

# Define our class. Class accepts arguments restaurant_name and cuisine_type. 
# Self is there but self is the name of the instance of the class. 
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

chez_bob = Restaurant('Chez Bob', 'French')
chez_bob.set_number_served(10)
chez_bob.increment_number_served(20)
chez_bob.describe_restaurant()







class User():
    def __init__(self, first_name, last_name, zip, age):
        """ Create a user an accept f & l name, zip, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.zip = zip
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print("You are " + self.first_name.title() + " " + self.last_name.title() +
                " and you are " + str(self.age) + " years old and live in " + 
                str(self.zip) + " zip code.")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

bob = User('bob', 'bobberson', '1111', 22)
print(bob.login_attempts)
bob.increment_login_attempts()
bob.increment_login_attempts()
bob.increment_login_attempts()
bob.increment_login_attempts()
print(bob.login_attempts)
bob.reset_login_attempts()
print(bob.login_attempts)

    



