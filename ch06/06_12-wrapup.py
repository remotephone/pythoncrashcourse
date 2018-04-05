# pets
pets = {
    'rufus': {
        'type': 'dog',
        'owner': 'tim',
    },
    'kitty': {
        'type': 'cat',
        'owner': 'bill',
    },
    'bubbles': {
        'type': 'fish',
        'owner': 'jen',
    }
}

for pet, facts in pets.items():
    print(pet.title() + " is a " + facts['type'] + " owned by " +
          facts['owner'].title() + ".")


# favorite places

favorite_places = {
    'bob': 'usa',
    'jen': 'mexico',
    'tina': 'canada',
}

for k, v in favorite_places.items():
    if v == 'usa':
        print(k.title() + "'s favorite place is " + v.upper() + ".")
    else:
        print(k.title() + "'s favorite place is " + v.title() + ".")
    
# numbers

nums = {
    'bob': ['1', '3'],
    'tim': ['2', '4'],
    'sue': ['3', '5'],
    'jan': ['4', '6'],
    'joe': ['5', '7']
}

for k, v in nums.items():
    print(k.title() + "'s favorite numbers are " + str(v))



cities = {
    'milan': {
        'country': 'italy',
        'popu': 10,
        'fact': 'fashion',
        },
    'berlin': {
        'country': 'germany',
        'popu': 12,
        'fact': 'capitol',
    }
}

for city, stuff in cities.items():
    print(city.title() + " has " + str(stuff['popu']) + " people in it and is known\
 for being the " + stuff['fact'] + "-capital of " + stuff['country'].title() + ".")