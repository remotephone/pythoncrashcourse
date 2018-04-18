import json

# Load the username if its been stored previously.
# Otherwise prompt for the username and store it.
filename = 'username.json'

# Try to open the file 
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)

# If the file doesn't exist, prompt user for input and write it to file.
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        # write username input to file
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")

else:
    print("Welcome back, " + username + "!")