def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willy')
describe_pet(pet_name='tim', animal_type='cat')

"""
try:
    describe_pet()
except:
    print("I need a name and type")
"""