players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("We can print 0 to 3, 1 to 4, and beginning to 4")
print(players[0:3])
print(players[1:4])
print(players[:4])
print("\n")

print("We can also print 2 to end with [2:] and 3 from the end to end with [-3:]")
print(players[2:])
print(players[-3:])

print("We can also loop through a slice of a list:")
for player in players[:3]:
    print(player.title())

