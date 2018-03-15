users = ['user1', 'user2', 'admin', 'user3', 'user4']

# users = []

if users:
    for user in users:
        if user != 'admin':
            print("You can't come in " + user)
        else:
            print("Come on in admin")


current_users = ['user1', 'user2', 'user3', 'user4', 'user5']
new_users = ['user6', 'user7', 'user8', 'user9', 'user1']

for userz in new_users:
    if userz in current_users:
        print(userz + " already exists")

numbers = list(range(1,9))
for num in numbers:
    if num == 1:
        print(str(num) + "st")
    elif num == 2:
        print(str(num) + "nd")
    elif num == 3:
        print(str(num) + "rd")
    else:
        print(str(num) + "th")