# 2. Faça um programa que converta a moeda REAL em DÓLAR

# real = float(input('Digite o valor em real: '))

# convercao = real / 5.70

# print(convercao)

def convercao(real):
    convercao = real / 5.86
    return round(convercao, 2)
print(convercao(100))
