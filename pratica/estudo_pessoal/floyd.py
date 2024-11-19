import os


os.system('cls')

count = 0
for i in range(1, 5):
    print(' ' * (5-i), end= '|')
    for j in range(i):
        count += 1
        print(count, end = '|')
    print()
