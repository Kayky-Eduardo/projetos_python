import os
import copy

os.system('cls')


d1 = {
    'nome': 'kayky',
    'email': 'Jos@',
    'num': [1, 2, 3]
}

d2 = d1.copy()
d1['num'] = tuple(d1['num'])
d2['num'][1] = 10
d1['num'] = list(d1['num'])
print(d1)
print(d2)