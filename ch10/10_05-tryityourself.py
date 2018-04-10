# Specify the file with the contents you wanna read.
txtfile = 'learning_python.txt'

# open the file and assign them to contents
with open(txtfile) as contents:
    # assign readlines() of contents to lines. 
    lines = contents.readlines()

# blank knowledge as a placeholder.
knowledge = ''
# for loop through the items in it and add them to line.
for line in lines:
    knowledge += line
    # to do the second exercise we replace. 
    # knowledge += line.replace('Python', 'Ruby')
    
# print it times 3
print(knowledge * 3)
