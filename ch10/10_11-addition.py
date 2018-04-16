try:
    num1 = input("Give me the first number: ")
    num1 = int(num1)
    num2 = input("Give me the 2nd number: ")
    num2 = int(num2)

except ValueError:
    print("You gotta give two numbers.")

else:
    sum = num1 + num2
    print(sum)