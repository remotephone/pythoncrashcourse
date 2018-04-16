books = ['frankenstein.txt', 'heartofdarkness.txt', 'prideandprejudice.txt']

for book in books:
    with open(book) as content:
         words = content.read()
         lowers = words.lower()
         amount = lowers.count('the')
         print(amount)