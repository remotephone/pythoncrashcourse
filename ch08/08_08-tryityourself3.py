"""
# city names

def city_country(city, country):
    return city.title() + ", " + country.title()
# pretty simple but just did this 2 different ways. print simply.
print(city_country('havana', 'cuba'))
# define two and then print them.
pair2 = city_country('milan', 'italy')
pair3 = city_country('paris', 'france')
print(pair2)
print(pair3)


"""

"""
def make_album(artist, title):
    album = {'musician': artist, 'record': title}
    return album

# give the user 3 changes to define an album. This is clunky.
singer = input("Who made this first recording? ")
albumname = input("What is it called?")

singer2 = input("Who made this second recording? ")
albumname2 = input("What is it called?")

singer3 = input("Who made this third recording? ")
albumname3 = input("What is it called?")

# set the user input to different variables made from the function
thehits1 = make_album(singer, albumname)
thehits2 = make_album(singer2, albumname2)
thehits3 = make_album(singer3, albumname3)

# print the resulting data. 
print(thehits1)
print(thehits2)
print(thehits3)
"""
# create you function that makes a dictionary.
def make_album(artist, title):
    album = {'musician': artist, 'record': title}
    return album

# start a while loop.
while True:
    print("(enter 'q' at any time to quit)")
    # user input goes to singer and albumname. Not using make_album() yet.
    singer = input("What is the artists name? ")
    if singer == 'q':
        break
    albumname = input("What is the records name? ")
    if albumname == 'q':
        break
    
    # define record as the result of make_album(). Now we're using the function.
    record = make_album(singer, albumname)
    # Call the values ("artists") from the keys ("musician") from record. 
    print("The album " + record['musician'].title() + " was made by "\
          + record['record'].title() + ".")
    