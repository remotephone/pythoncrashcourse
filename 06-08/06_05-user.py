user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
print("""
for key, value in user_0.items():
    print("\nKey: " +  key)
    print("Value: " + value)
""")

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

print("""
for k, v in user_0.items():
    print("\nKey: " +  key)
    print("Value: " + value)
""")

for k, v in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
