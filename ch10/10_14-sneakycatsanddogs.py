files = ['dog.txt', 'cat.txt']


for file in files:

    try:
        with open(file) as f:
            names = f.readlines()

    except FileNotFoundError:
        pass
        
    else:
        for name in names:
            print("My pet's name is " +  name.rstrip())
