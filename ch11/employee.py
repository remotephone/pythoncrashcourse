class Employee():
    """A person with a job that gets money"""

# Assign your stuff. we're titling the name.
    def __init__(self, first, last, salary):
        """CREATE LIFE"""
        self.first = first.title()
        self.last = last.title()
        self.salary = salary

# This can be this simple, just add the amount to the salary.
# I had tried to do an if amount: bit, but it's not needed for this
    def give_raise(self, amount=5000):
            self.salary += amount
