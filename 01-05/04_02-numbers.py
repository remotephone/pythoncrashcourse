print("range(1,5) actually prints 1-4 because it gets to 5 and stops.")
for value in range(1,5):
    print(value)
print("range(1,5) actually prints 1-4 because it gets to 5 and stops.")
for value in range(1,6):
    print(value)
print(value)

even_numbers = list(range(2,11,2))
print(even_numbers)

print("\n")

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

squares2 = []
for value in range(1,11):
    squares2.append(value**2)

print(squares)


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("This is our list of digits: " + str(digits))
print("We print min, max and sum now.")
print(min(digits))
print(max(digits))
print(sum(digits))

squares3 = [value**2 for value in range(1,11)]
print(squares3)

squares4 = [value**2 for value in range(2,11,2)]
print(squares4)