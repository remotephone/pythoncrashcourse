for num in range(1,21):
    print(num)

print("One Million works, but commented it out for brevity. It looks like this:")
print("""
for miln in range(1,1000001):
    print(miln)
""")

miln = list(range(1,1000001))
print(min(miln))
print(max(miln))
print(sum(miln))

odds = list(range(1,20,2))
print(odds)

threes = list(range(0,30,3))
for three in threes:
    print(three)


cubed =[]
for value in range(1,11):
    cubed.append(value**3)
print(cubed)
cubes = [value**3 for value in range(1,11)]
print(cubes)