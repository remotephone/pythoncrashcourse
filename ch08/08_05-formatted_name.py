# Create a function called get_format_name with first and last name
def get_formatted_name(first_name, last_name):
    # Describe the function
    """Return a full name, neatly formatted."""
    # The names are joined into full name
    formatted_name = first_name + ' ' + last_name
    # return the value, don't do anything with it yet
    return formatted_name.title()

def get_full_name(first_name, middle_name, last_name):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

# Take function and assign it to musician
musician1 = get_formatted_name('jimi', 'hendrix')
musician2 = get_full_name('john', 'lee', 'hooker')
# I still have to specify a middle name, ?? It's not truly optional this way.
musician3 = get_full_name('jimi', '', 'hendrix')
print(musician1)
print(musician2)
print(musician3)
