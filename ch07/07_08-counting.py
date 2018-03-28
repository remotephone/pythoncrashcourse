current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
# Return to the beginning of the loop. we skip printing it and just go back.
        continue
    
    print(current_number)

print("\nSimple count now.")

x = 1
while x <= 5:
    print(x)
    x += 1