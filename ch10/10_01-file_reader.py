# check the directory you're in and open pi_digits.txt as file_object
with open('pi_digits.txt') as file_object:
    # read it and assign it to contents
    contents = file_object.read()
    # print file, stripping white space to the right
    print(contents.rstrip())