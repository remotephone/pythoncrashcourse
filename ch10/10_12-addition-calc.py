print('Say quit when done.')
while True:
    try:
        num1 = input("Give me the first number: ")
        if num1 == 'quit':
            break
        num1 = int(num1)

        num2 = input("Give me the 2nd number: ")
        if num2 == 'quit':
            break
        num2 = int(num2)

    except ValueError:
        print("You gotta give two numbers.")

    else:
        sum = num1 + num2
        print(sum)
