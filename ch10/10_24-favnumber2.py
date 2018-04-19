import json

# Get ready to print the number if it's there.
print("Your favorite number is...")

# Try except so this works if it's ther eand doesn't if its not.
try:
    # open the file num.txt as num
    number = 'num.txt'
    with open(number) as num:
        # assign content of file to number
        number = json.load(num)
        # print it if it's there.
        print(number + "!")
# If we don't find the file, do thi sstuff.
except FileNotFoundError:
    # prompt for number, save as favs
    favs = input("I don't know it. What is your favorite number? ")
    # open num.txt for writing and dump data into it.
    with open('num.txt', 'w') as file:
        json.dump(favs, file)
    # print what it was. 
    print("Ok your number is " + favs + "!")
