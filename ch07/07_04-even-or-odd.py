number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

print("\n===================\n")

car = input("What type of car would you like to rent? ")
print("OK, lemme see if I can find you a " + car.title() + ".")

print("\n===================\n")

guests = input("How many people are in your party? ")
guests = int(guests)
if guests > 8:
    print("You'll need to wait for your table.")
else:
    print("Right this way people.")

print("\n===================\n")

num = input("Gimme a number: ")
num = int(num)
if num % 10 == 0:
    print("This is divisible by ten!")
else:
    print("This is not divisible by ten.")