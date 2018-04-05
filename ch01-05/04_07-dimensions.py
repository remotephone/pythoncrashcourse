#tuple is a list that cannot change. Immutable List!

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

""" This won't work because tuples are immutable:
dimensions[0] = 250
"""


print("Original Dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified Dimensions:")
for dimension in dimensions:
    print(dimension)

foods = ('cheese', 'taco', 'rice', 'bean', 'soup')
for food in foods:
    print(food)
# foods[0] = 'taters'

foods = ('egg', 'water', 'rice', 'bean', 'soup')
for food in foods:
    print(food)