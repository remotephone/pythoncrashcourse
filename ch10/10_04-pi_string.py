file_name = 'pi_million_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

#print(pi_string[:52] + "...")
#print(len(pi_string))

birthday = input("Enter your bday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday is in the first million digits of pi!")
else:
    print("Sorry, your birthday doesn't show up in pi yet.")