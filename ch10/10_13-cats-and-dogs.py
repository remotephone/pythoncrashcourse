# This works just fine for two files, but doesn't handle errors well or more than 
# two files. 

# # Try to open both files, don't do anything else
# try:
#     with open('dog.txt') as dogs:
#         # Use readlines to pull each line from file.
#         dognames = dogs.readlines()
#     with open('cat.txt') as cats:
#         catnames = cats.readlines()

# except FileNotFoundError:
#     print("Where my dogs/cats at?")

# else:
#     for catname in catnames:
#         # rstrip() to remove blank line.
#         print("I got a cat named " + catname.rstrip())
#     for dogname in dognames:
#         print("I got a dog named " + dogname.rstrip())
    

    
files = ['dog.txt', 'cat.txt']


for file in files:

    try:
        with open(file) as f:
            names = f.readlines()

    except FileNotFoundError:
        print("I can't find a file.")
        
    else:
        for name in names:
            print("My pet's name is " +  name.rstrip())
