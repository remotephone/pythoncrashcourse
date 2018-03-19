# Copying old code

defs = {
    'list': 'a list of items, mutable',
    'dictionary': 'a list of key value pairs, mutable',
    'tuple': 'immutable list',
    'for loop': 'perform action on sequential list of item',
    'if': 'conditional statement',
}

print("These are some things I learned: \nlist:\t\t" + defs['list'] +
      "\n" + "dictionary:\t" + defs['dictionary'] + "\ntuple:\t\t" +
      defs['tuple'] + "\nfor loop:\t" + defs['for loop'] +
      "\nif:\t\t" + defs['if'])


print("These are some things I learned: ")
for k, v in defs.items():
    print(k + ": " + v)
