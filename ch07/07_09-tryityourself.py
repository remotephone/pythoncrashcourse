"""
print("Enter your toppings:")
toppings = []
while toppings != 'quit':
    toppings = input("topping: ")
    print("I'll add " + toppings + " to your pizza.")
"""

"""
# first set the age to 0
age = 0
# test age = 0
while age == 0:
# ask for the age
    age = input("How old are you? Tell me 'quit' to quit.\n")
# if they're old, just end the loop.
    if age = 'quit':
        print("Ok come back any time.")
        break
# test for ages and values. Set age to ineger each time.
    elif int(age) < 3:
        price = 0
    elif int(age) < 12:
        price = 10
# if anything over 12, set price to 15.
    else:
        price = 15

    print("Your ticket costs $" + str(price) + ".")

"""
import sys

x = 3
while x > 2:
    x += 1
# Here is a fancy trick to print on a single line over and over.
    print(str(x) + "\r", end="")