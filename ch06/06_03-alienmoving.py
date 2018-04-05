alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))



# Now we set the speed to fast instead
alien_0['speed'] = 'fast'


# Move the alien to the right.
# Determine how far to move alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

print("\nThis is alien_1 now!")
alien_1 = {'color': 'green', 'points': 5}
print(alien_1)

del alien_1['points']
print(alien_1)