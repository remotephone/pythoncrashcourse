import json 

number = 'num.txt'

with open(number) as num:
    number = json.load(num)
    print("Your favorite number is " + number + "!")