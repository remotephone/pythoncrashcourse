responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would yuou like to let another person response? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete, show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response.title() + ".")