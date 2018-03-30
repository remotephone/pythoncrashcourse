# Create a function make_shirt. Give it a message and default size small
def make_shirt(message, size='small'):
    print("You get a " + size + " shirt with \"" + message +
    "\" printed on it.")

# make a shirt with message wow go me and size large
make_shirt('wow go me', 'large')
# make a shirt medium and Utah is for lovers
make_shirt(size='medium', message='Utah is for lovers.')


# This is a different function. Create  city in Italy.
def describe_city(city, country='italy'):
    print(city.title() + " is in " + country.title() + ".")

describe_city('milan')
describe_city('rome')
describe_city('beijing', 'china')
