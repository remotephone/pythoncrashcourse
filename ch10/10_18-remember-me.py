import json

# Prompt for name with input
username = input("What is your name? ")

filename = 'username.json'
# open filename and write to it
with open(filename, 'w') as f_obj:
    # write data from username to file
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
