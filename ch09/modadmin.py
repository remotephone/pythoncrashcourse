from moduser import User

class Admin(User):
    """This is a special user with special rights."""
    def __init__(self, first_name, last_name, zip, age):
        """Initialize attributes of the parent class."""
        super().__init__(first_name, last_name, zip, age)
        self.privs = Privileges()


class Privileges():
    """This is a special user with special rights."""
    def __init__(self):
        """Initialize attributes of the parent class."""
        self.privs = ['read', 'write', 'delete']

    def show_privs(self):
        print(self.privs) 