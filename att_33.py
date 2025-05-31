print("--- Padrão 1: Canto Superior Esquerdo (2x2) ---")

matriz_A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

soma_padrao1 = 0

print("Matriz A:")
for i in range(4):
    for j in range(4):
        print(f"{matriz_A[i][j]:4}", end="") 
    print() 

print("\nElementos marcados com 'X' no Padrão 1:")
for i in range(4):
    for j in range(4): 
        if (i == 0 and (j == 0 or j == 1)) or \
           (i == 1 and (j == 0 or j == 1)):
            soma_padrao1 = soma_padrao1 + matriz_A[i][j]
            print(f"A[{i}][{j}] = {matriz_A[i][j]}")

print(f"\nSoma dos elementos do Padrão 1: {soma_padrao1}")

print("-" * 40)

print("--- Padrão 2: Canto Inferior Direito (2x2) ---")


matriz_A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

soma_padrao2 = 0

print("Matriz A:")
for i in range(4):
    for j in range(4):
        print(f"{matriz_A[i][j]:4}", end="")
    print()

print("\nElementos marcados com 'X' no Padrão 2:")

for i in range(4): 
    for j in range(4): 
       
        if (i == 2 and (j == 2 or j == 3)) or \
           (i == 3 and (j == 2 or j == 3)):
            soma_padrao2 = soma_padrao2 + matriz_A[i][j]
            print(f"A[{i}][{j}] = {matriz_A[i][j]}")

print(f"\nSoma dos elementos do Padrão 2: {soma_padrao2}")

print("-" * 40) 

print("--- Padrão 3: Diagonal Inferior Esquerda ---")


matriz_A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

soma_padrao3 = 0

print("Matriz A:")
for i in range(4):
    for j in range(4):
        print(f"{matriz_A[i][j]:4}", end="")
    print()

print("\nElementos marcados com 'X' no Padrão 3:")


for i in range(4):
    for j in range(4): 
        if j <= i:
            soma_padrao3 = soma_padrao3 + matriz_A[i][j]
            print(f"A[{i}][{j}] = {matriz_A[i][j]}")

print(f"\nSoma dos elementos do Padrão 3: {soma_padrao3}")

print("-" * 40) 

print("--- Padrão 4: Diagonal Superior Direita ---")


matriz_A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

soma_padrao4 = 0

LINHAS = 4
COLUNAS = 4

print("Matriz A:")
for i in range(LINHAS):
    for j in range(COLUNAS):
        print(f"{matriz_A[i][j]:4}", end="")
    print()

print("\nElementos marcados com 'X' no Padrão 4:")


for i in range(LINHAS): 
    for j in range(COLUNAS): 
        if j > i: 
            soma_padrao4 = soma_padrao4 + matriz_A[i][j]
            print(f"A[{i}][{j}] = {matriz_A[i][j]}")

print(f"\nSoma dos elementos do Padrão 4: {soma_padrao4}")

print("-" * 40)