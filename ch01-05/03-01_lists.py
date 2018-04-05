bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print("Printing the whole list first")
print(bicycles)
print("========\n")

print("Now just printing the first object, 0")
print(bicycles[0])

print("========\n")
print("Now just printing and titlizing the first object, 0")
print(bicycles[0].title())

print("========\n")
print("printing bicycles 1 and 3, actually 2 and 4")
print(bicycles[1])
print(bicycles[3])

print("========\n")
print("printing bicycles last, 2nd to last, and 3rd to last")
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])



message = "My first bicycle was a " + bicycles[0].title() + "."

print(message)
