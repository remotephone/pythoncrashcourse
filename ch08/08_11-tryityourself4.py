
# Make your list
magicians = ['tim', 'joe', 'bob']

"""
# Makes a function that prints your argument
def show_magicians(magicians):
    print(magicians)

# print it
show_magicians(magicians)

"""
"""
# Making a function that pulls the last magician and appends The GREAT to it
def make_great(magicians):
    while magicians:
        magician = magicians.pop() + " The Great"
        print(magician.title())

make_great(magicians)

"""
# New function, same as above
def make_great(magicians):
    while magicians:
        magician = magicians.pop() + " The Great"
        print(magician.title())

# Does the same thing with a copy of the list instead of the list itself. 
make_great(magicians[:])
print(magicians)
