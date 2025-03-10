# 20-Solicite ao usuário que insira os elementos de uma matriz 3x3 e exiba a matriz formatada.

matriz = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
]

for linha in range(3):
    for coluna in range(3):
        valores = int(input(f'Digite o valor para a posição [{linha}][{coluna}]: '))
        matriz[linha][coluna] = valores


for linha in matriz:
    print(linha)