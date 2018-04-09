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


