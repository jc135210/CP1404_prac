for i in range(1, 21, 2):
    print(i, end=' ')
print()
for i in range(0, 101, 10):
    print(i, end=' ')
print()
for i in range(20, 0, -1):
    print(i, end=' ')
print()
star_value = int(input('enter a number: '))
for i in range(1, star_value + 1):
    print('*', end=' ')
print()
for i in range(1, star_value + 1):
    print('*' * i)
print()

