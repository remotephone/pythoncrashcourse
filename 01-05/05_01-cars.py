# Simplemente!
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Conditional tests
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# ignoring case
print("Check if Audi == audi and strict check")
lowcar = 'audi'
car = 'Audi'
if lowcar == car:
    print("samesies")
else:
    print("different")

print("Lower case on both and see if they're the same now")
if lowcar.lower() == car.lower():
    print("samesies")
else:
    print("different")
