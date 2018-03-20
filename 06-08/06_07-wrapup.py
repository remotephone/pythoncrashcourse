# Copying old code

defs = {
    'list': 'a list of items, mutable',
    'dictionary': 'a list of key value pairs, mutable',
    'tuple': 'immutable list',
    'for loop': 'perform action on sequential list of item',
    'if': 'conditional statement',
}



print("These are some things I learned: ")
for k, v in defs.items():
    print(k + ": " + v)

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'rhine': 'germany',
}

for k, v in rivers.items():
    print("The " + k.title() + " runs through " + v.title() + ".")


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people = ['jen', 'sarah', 'edward', 'kim', 'tim', 'jane', 'phil']

for ppl in favorite_languages.keys():
    if ppl in people:
        print(ppl.title() + " took the poll.")
        
for nots in people:
    if nots not in favorite_languages.keys():
        print(ppl.title() + " needs to take the poll.")