magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

print("\n====================")
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you everyone, that was a great show!")
print("\n====================\n")

print ("""This is improperly formatted code:\n
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician)\n

It should look like this:\n
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)\n
""")

print("Now for pizza stuff")

pizza = ['pepperoni', 'cheese', 'olive']
for za in pizza:
    print("I like " + za + " pizza.")
print("I really like pizza!\n")


print("Now for animals")

animals = ['dog', 'cat', 'snek']
for animal in animals:
    print("I would like to boop a " + animal + ".")
print("That would be nice")