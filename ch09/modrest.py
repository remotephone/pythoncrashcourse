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


class IceCreamStand(Restaurant):
    """Represents an Ice Cream Stand Restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'honey']

    def flavor_list(self):
        print(self.flavors)