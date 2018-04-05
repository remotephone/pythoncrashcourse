print("Creating a list first.")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

print("Then we remove an object...")
motorcycles.remove('ducati')
print(motorcycles)

print("Using the original list, let's remove and print.")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
