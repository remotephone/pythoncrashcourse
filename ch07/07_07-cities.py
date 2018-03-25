prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
# changed this so you could put lower in any case.
    if city.lower() == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")