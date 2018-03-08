print("Let's print the first list of motorcycles.")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

print("========\n")
print("Now we update the first one and print the list again.")
motorcycles[0] = 'ducati'
print(motorcycles)

print("========\n")
print("Now let's add one more to the list.")
motorcycles.append('harley')
print(motorcycles)

print("========\n")
print("Now we clear the list")
motorcycles = []
print(motorcycles)

print("========\n")
print("Now we add items to the list with with append() and get:")

motorcycles.append('honda-new')
motorcycles.append('yamaha-new')
motorcycles.append('suzuki-new')

print(motorcycles)

print("========\n")
print("Now we'll insert an element into the list.")
motorcycles.insert(0, 'ducati-new')
print(motorcycles)

print("========\n")
print("Now we'll remove it.")
del motorcycles[0]
print(motorcycles)

print("========\n")
print("First we pop the last item off the list, print the list and the popped item.")
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print("We can also use that item")
print("The last motocycle I bought was a " + popped_motorcycle + ".")
print("That's weird, so let's drop the new with split(), but we need to strigify and call the right item.")
print("The last motocycle I bought was a " + str(popped_motorcycle.split("-")[0]) + ".")