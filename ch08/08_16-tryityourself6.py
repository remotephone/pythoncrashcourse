import printingfunctions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models =[]

# Do your stuff.
pf.print_models(unprinted_designs, completed_models)
#This will also work, but it copies the list and ends up with the value not 
# being emptied
#print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)
print(unprinted_designs)
print(completed_models)