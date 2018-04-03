# Importing capwords because title() causes Bob'S
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
    
    # each instance gets this method available to it. the method prints both args
    # in a sentence. The self tells all characteristics associated with self (the class)
    # are available to it. 
    def describe_restaurant(self):
        print("Welcome to " + capwords(self.restaurant_name) + " where we make " +
                self.cuisine_type + " food.")

    # Each instance also gets this method. It only uses the r_n arg. 
    def open_restaurant(self):
        print(capwords(self.restaurant_name) + " is now open!")

# First instance of a class. It's name restaurant which isn't clear.
# print each class instance. class.method
restaurant = Restaurant("bob's", "bbq")
# print the args from the class __init__ method.
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()

# Second instance of the class. holeinwall is clearer than restaurant since it doesn't
# share a name. It get's two different arguments.
holeinwall = Restaurant("marge's", "diner")
# Do it again.
print(holeinwall.restaurant_name)
print(holeinwall.cuisine_type)
holeinwall.describe_restaurant()

# Second instance of the class. holeinwall is clearer than restaurant since it doesn't
# share a name. It get's two different arguments.
fancy = Restaurant("pierre's", "escargot")
# Do it again.
print(fancy.restaurant_name)
print(fancy.cuisine_type)
fancy.describe_restaurant()



class User():
    def __init__(self, first_name, last_name, zip, age):
        """ Create a user an accept f & l name, zip, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.zip = zip
        self.age = age

    def describe_user(self):
        print("You are " + self.first_name.title() + " " + self.last_name.title() +
                " and you are " + str(self.age) + " years old and live in " + 
                str(self.zip) + " zip code.")

tim = User("tim", "timmers", "11111", 11)   
tim.describe_user()

bob = User("bob", "bobbers", "22222", 22)   
bob.describe_user()

jen = User("jen", "jenners", "33333", 33)   
jen.describe_user()
