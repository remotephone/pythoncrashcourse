# Simple example of try except 
#try:
#    print(5/0)
#except ZeroDivisionError:
#    print("You can't divide by zero!")

# Give them some guidance
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

# While loop. As long as you're giving them something it'll work.
while True:
    # Take 2 numbers, quit if a number is q
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    # convert both numbers to integers and divide them.
    # do this in try except to catch errors. This only catches one type of error
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero.")
    else:
        print(answer)