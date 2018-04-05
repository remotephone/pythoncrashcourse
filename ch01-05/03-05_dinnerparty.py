guests = ['sam adams', 'joe dirt', 'julius caeser', 'ben franklin']
print(guests[0].title() + ", please attend my dinner.")
print(guests[1].title() + ", please attend my dinner party.")
print(guests[2].title() + ", I am having a party. Please attend.")
print("Please attend my dinner, " + guests[3].title() + "." )


print("Looks like " + guests[0].title() + " can't make it.")
popped = guests.pop(0)
guests.insert(0, "rosa parks")
print("We'll remove " + popped + " and invite " + guests[0].title())
print(guests)

print(guests[0].title() + ", please attend my dinner.")
print(guests[1].title() + ", please attend my dinner party.")
print(guests[2].title() + ", I am having a party. Please attend.")
print("Please attend my dinner, " + guests[3].title() + "." )

print("Let's add more people!")
guests.insert(0, "dorito bandito")
guests.insert(2, "mad max")
guests.append("gypsy danger")

print("Our new list is " + str(guests).title())

print("Oh no I only have 2 chairs!")
popped1 = guests.pop()
print("Sorry " + popped1.title() + ", there's no room.")
popped2 = guests.pop()
print("Sorry " + popped2.title() + ", there's no room for you either.")
popped3 = guests.pop()
print("Sorry " + popped3.title() + ", you gotta go.")
popped4 = guests.pop()
print("Sorry " + popped4.title() + ", you can't come.")
popped5 = guests.pop()
print("Sorry " + popped5.title() + ", you have no chair.")

print("Looks like it's just me, " + guests[0].title() + ", and " + guests[1].title() + ".")
del guests[1]
del guests[0]
print("Once they leave, this is my list.")

print(guests)