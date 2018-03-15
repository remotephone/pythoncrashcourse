# you can copy a list with the list[:]
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# then you can append values individually to each copied list. The copied base remains the same. 
my_foods.append('cannoli')
friend_foods.append('salad')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)