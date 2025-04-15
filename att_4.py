#  4. Faça um programa que calcule a área de um círculo. 

# raio = float(input('Digite o valor do raio: '))

# diametro = 3.14 * raio ** 2

# print(diametro)

def calcular_area_circulo(raio):
    diametro = 3.14 * raio **2
    return diametro

print(calcular_area_circulo(12.2))