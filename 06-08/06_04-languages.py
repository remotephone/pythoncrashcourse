favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")

print("Trying it myself....")
person = {
    'first': 'bob',
    'last': 'bobertson',
    'age': '21',
    'city': 'boston',
}

print("Meet " + person['first'].title() + " " + person['last'].title() +
      " who is " + str(person['age']) + " years old and lives in " +
       person['city'].title() + ".")

nums = {
    'bob': '1',
    'tim': '2',
    'sue': '3',
    'jan': '4',
    'joe': '5',
}

print(nums)

defs = {
    'list': 'a list of items, mutable',
    'dictionary': 'a list of key value pairs, mutable',
    'tuple': 'immutable list',
    'for loop': 'perform action on sequential list of item',
    'if': 'conditional statement',
}

print("These are some things I learned: \nlist:\t\t" + defs['list'] +
      "\n" + "dictionary:\t" + defs['dictionary'] + "\ntuple:\t\t" + defs['tuple'] +
      "\nfor loop:\t" + defs['for loop'] + "\nif:\t\t" + defs['if'])
