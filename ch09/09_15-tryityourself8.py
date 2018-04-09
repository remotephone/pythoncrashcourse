from random import randint

class Die():
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        results = randint(1, self.sides)
        print(results)

roll = Die(6)
roll.roll_die()


roll2 = Die(20)
roll2.roll_die()