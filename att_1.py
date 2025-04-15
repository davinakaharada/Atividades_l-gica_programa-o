# 1. Faça um programa que receba 5 notas, calcule a média aritmética destas notas e apresente o resultado

# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a primeira nota: '))
# n3 = float(input('Digite a primeira nota: '))
# n4 = float(input('Digite a primeira nota: '))
# n5 = float(input('Digite a primeira nota: '))

# media = (n1+n2+n3+n4+n5) / 5

# print(media)

def calcular_notas():
    contador = 0
    soma = 0
    while contador < 5:
        notas = int(input('Digite as notas: '))
        soma = soma+notas
        contador +=1
    media = soma / 5   
    return media

print(calcular_notas())

