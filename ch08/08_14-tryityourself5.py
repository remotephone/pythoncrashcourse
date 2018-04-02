"""
# Create your function and assign it the wildcard items argument
def sandwich_items(*toppings):
    # for loop to bring in each item.
    for topping in toppings:
        return toppings

sandwich1 = sandwich_items('bacon', 'lettuce', 'tomato', 'cheese')
sandwich2 = sandwich_items('bacon', 'lettuce', 'mustard')
sandwich3 = sandwich_items('bacon', 'lettuce')

print(sandwich1)
print(sandwich2)
print(sandwich3)

"""
"""

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('tim', 'smith', style='swarthy', hat='trilby',
                             hair='wavy')

print(user_profile)
"""

def make_car(make, model, **trim):
# This would work if we just wanna submit arbitrary trim values
# def make_car(**trim):
    car = {}
#   If just doing trim values, you can't add other key pairs.
    car['make'] = make
    car['model'] = model
    for key, value in trim.items():
        car[key] = value
    return car


made_car = make_car('subaru', 'outback', color='blue', tow_package=True)
# This would pass all arguments as key value pairs of trim().
# made_car = make_car(make='subaru', model='outback', color='blue', tow_package=True)

print(made_car)