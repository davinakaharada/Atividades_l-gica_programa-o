# 31. Ler uma matriz M 5 x 5, calcular e escrever as seguintes somas: d) da diagonal secundária

matriz = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]

lista = []
for linha in range(5):
    lista.append(matriz[linha][4-linha])
soma = sum(lista)

print(lista)
print(soma)