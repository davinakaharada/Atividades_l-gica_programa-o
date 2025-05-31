# 32.	 Ler 2 matrizes, A 4 x 6 e B 4 x 6 e criar:
# b) uma matriz D que seja a diferença de A e B. (A – B).
# Escrever as matrizes S e D após todo cálculo estar concluído.

matriz_A = [
    [10, 20, 30, 40, 50, 60],
    [70, 80, 90, 100, 110, 120],
    [130, 140, 150, 160, 170, 180],
    [190, 200, 210, 220, 230, 240]
]

matriz_B = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24]
]


LINHAS = 4
COLUNAS = 6


print("--- Matriz A ---")
for i in range(LINHAS): 
    for j in range(COLUNAS): 
        print(f"{matriz_A[i][j]:5}", end="")
    print() 


print("\n--- Matriz B ---")
for i in range(LINHAS):
    for j in range(COLUNAS):
        print(f"{matriz_B[i][j]:5}", end="")
    print()


matriz_S = []
for i in range(LINHAS):
    nova_linha = []
    for j in range(COLUNAS):
        nova_linha.append(matriz_A[i][j] + matriz_B[i][j])
    matriz_S.append(nova_linha)


matriz_D = []
for i in range(LINHAS):
    nova_linha = []
    for j in range(COLUNAS):
        nova_linha.append(matriz_A[i][j] - matriz_B[i][j])
    matriz_D.append(nova_linha)


print("\n--- Matriz S (A + B) ---")
for i in range(LINHAS):
    for j in range(COLUNAS):
        print(f"{matriz_S[i][j]:5}", end="")
    print()

print("\n--- Matriz D (A - B) ---")
for i in range(LINHAS):
    for j in range(COLUNAS):
        print(f"{matriz_D[i][j]:5}", end="")
    print()