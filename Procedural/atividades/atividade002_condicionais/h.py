import os


os.system('cls')

a = 1
b = -6
c = 5

#vou fazer por delta e bhaskara
#calculo do delta
delta = (b * b) - (4 * a * c)
 
#calculo bhaskara
raiz1 = (-b + delta **(1/2)) / (2 * a)
raiz2 = (-b - delta **(1/2)) / (2 * a)

print(f'As raízes são {raiz1} e {raiz2}')