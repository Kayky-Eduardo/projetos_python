import math

def calcular_area_circulo(raio):
    return math.pi * raio ** 2

#solicita o raio ao usuario
raio = float(input("digite o raio do circulo: "))
area = calcular_area_circulo(raio)

print(f"A área do círculo com raio {raio} é: {area:.2f}")