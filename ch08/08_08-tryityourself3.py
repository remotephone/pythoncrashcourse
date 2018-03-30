"""
# city names

def city_country(city, country):
    return city.title() + ", " + country.title()

print(city_country('havana', 'cuba'))
pair2 = city_country('milan', 'italy')
pair3 = city_country('paris', 'france')
print(pair2)
print(pair3)


"""

"""
def make_album(artist, title):
    album = {'musician': artist, 'record': title}
    return album

singer = input("Who made this first recording? ")
albumname = input("What is it called?")

singer2 = input("Who made this second recording? ")
albumname2 = input("What is it called?")

singer3 = input("Who made this third recording? ")
albumname3 = input("What is it called?")

thehits1 = make_album(singer, albumname)
thehits2 = make_album(singer2, albumname2)
thehits3 = make_album(singer3, albumname3)

print(thehits1)
print(thehits2)
print(thehits3)
"""
def make_album(artist, title):
    album = {'musician': artist, 'record': title}
    return album

while True:
    print("(enter 'q' at any time to quit)")
    singer = input("What is the artists name? ")
    if singer == 'q':
        break
    albumname = input("What is the records name? ")
    if albumname == 'q':
        break
    
    record = make_album(singer, albumname)
    print("The album " + record['musician'].title() + " was made by "\
          + record['record'].title() + ".")
    