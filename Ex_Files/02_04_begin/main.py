NAMES = ["John", "Paul", "George", "Ringo", "Alex", "Joe Bob"]
AGES = [20, 21, 22, 23, 18, 45]
'''
i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

for name in NAMES:
    print(name)
'''
for name, age in zip(NAMES, AGES):
    print(f"{name} is {age} years old.")
'''
for name in reversed(NAMES):
    print(name)

for i in range(5):
    print(i)
'''
# enumerate

for i, name in enumerate(NAMES):
    print(f"{i}: {name}, {age}")
