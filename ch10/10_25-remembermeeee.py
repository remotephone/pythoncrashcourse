

import json

filename = 'username.json'

def get_stored_username():
    """Get stored username if available"""
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        check = input("Are you " + username + "? ")
        if 'yes' in check.lower():
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("Hello, " + username + "!")
    else:
        username = get_new_username()
        print("Hello, " + username + "!")


greet_user()
