# 32.	 Ler 2 matrizes, A 4 x 6 e B 4 x 6 e criar:
# a) uma matriz S que seja a soma de A e B.

# Definindo as matrizes A e B já preenchidas (4x6)
matriz_A = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24]
]

matriz_B = [
    [2, 2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5, 5]
]

linhas = 4
colunas = 6


print("--- Matriz A ---")
for linha in matriz_A:
    print(" ".join(f"{valor:7.0f}" for valor in linha)) 

print("\n--- Matriz B ---")
for linha in matriz_B:
    print(" ".join(f"{valor:7.0f}" for valor in linha)) 



print("\n--- Calculando a Matriz S (A + B) ---")


matriz_S = []
for i in range(linhas):
    matriz_S.append([0] * colunas) 


for i in range(linhas):
    for j in range(colunas):
        matriz_S[i][j] = matriz_A[i][j] + matriz_B[i][j]

print("\n--- Matriz S (A + B) ---")
for linha in matriz_S:
    print(" ".join(f"{valor:7.0f}" for valor in linha)) 