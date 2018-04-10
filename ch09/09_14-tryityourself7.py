from collections import OrderedDict

defs = OrderedDict()

defs['list'] = 'a list of items, mutable'
defs['dictionary'] = 'a list of key value pairs, mutable'
defs['tuple'] = 'immutable list'
defs['for loop'] = 'perform action on sequential list of item'
defs['if'] = 'conditional statement'


for k, v in defs.items():
    print("A " + k + " is a " + v + ".")

    