"""
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
"""

# This also works:

# Call the file as filename
filename = 'pi_digits.txt'

# open filename and store the contents as file_object
with open(filename) as file_object:
    # Read each line of file_object and store them as "lines" in a list
    lines = file_object.readlines()

# for loop through the lines and print them, removing trailing white space
for line in lines:
    print(line.rstrip())