import json

favs = input("What is your favorite number? ")

with open('num.txt', 'w') as file:
    json.dump(favs, file)