"""
# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Simulate printing a 3D print from a design
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
"""

# Create a function called print_models with the arguments unprinted_designs and
# completed_models.
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design until none are left.
    Move each design to completed_models after printing.
    """
# As long as you have unprinted designs, remove the last value with pop and 
# assign it to current designs. print that you did that, and then append it to 
# completed_models.
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from a design
        print("Printing model: " + current_design)
        completed_models.append(current_design)

# Make a for loop. Each item in completed_models will be printed. Completed
# models was generated above. 
def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# Two lists - completed_models is filled by the first function.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models =[]

# Do your stuff.
print_models(unprinted_designs, completed_models)
#This will also work, but it copies the list and ends up with the value not 
# being emptied
#print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
print(completed_models)