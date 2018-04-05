# We're using the players example from earlier.

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("We can print 0 to 3, 1 to 4, and beginning to 4")
print(players[0:3])
print(players[1:4])
print(players[:4])
print("\n")

print("We can also print 2 to end with [2:] and 3 from the end to end with [-3:]")
print(players[2:])
print(players[-3:])

print("We can also loop through a slice of a list:")
for player in players[:3]:
    print(player.title())


print("The first three items in the list are:")
print(players[:3])
print("Three items from the middle of the list are:")
print(players[2:5])
print("The last three items in the list are:")
print(players[-3:])



print("Now for pizza stuff")

pizza = ['pepperoni', 'cheese', 'olive']
"""
for za in pizza:
    print("I like " + za + " pizza.")
print("I really like pizza!\n")
"""
friend_pizza = pizza[:]
pizza.append('ham')
friend_pizza.append('taco')
print("My favorite pizzas are: ")
for za in pizza:
    print(za)
print("My friend's favorite pizzas are: ")
for fza in friend_pizza:
    print(fza)