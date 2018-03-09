print("Sorting the list alphabetically.")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)


print("Sorting reverse alphabetically.")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

print("Here is the original list:")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

print("Printing it again")
print(cars)

print("\nNow in reverse again using cars.reverse()")
cars.reverse()
print(cars)

print("\nNow the drill")
places = ['Italy', 'Germany', 'Mexico', 'Canada', 'Japan']
print(places)

print(sorted(places))
print(places)

places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)
places.sort(reverse=True)
print(places)


print(len(places))
