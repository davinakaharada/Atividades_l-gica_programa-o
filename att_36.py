# 36.	Ler uma matriz A 12 x 13 e divida todos os 13 elementos de cada uma das 12 linhas de A pelo valor do maior elemento daquela linha.
# Escrever a matriz A modificada.

print("--- Exercício 36: Matriz A Dividida pelo Maior da Linha ---")

LINHAS_A = 12
COLUNAS_A = 13

matriz_A_original = [
    [10, 20, 5, 30, 15],
    [2,  8,  1, 10, 4],
    [50, 5, 25, 10, 40],
    [3,  12, 6, 9, 1]
]

print("\nMatriz A Original (exemplo):")
for i in range(len(matriz_A_original)):
    for j in range(len(matriz_A_original[0])):
        print(f"{matriz_A_original[i][j]:5}", end="")
    print()

print("\nCalculando e modificando a Matriz A...")

for i in range(len(matriz_A_original)): 
    maior_elemento_na_linha = matriz_A_original[i][0] 

  
    for j in range(1, len(matriz_A_original[i])):
        if matriz_A_original[i][j] > maior_elemento_na_linha:
            maior_elemento_na_linha = matriz_A_original[i][j]

   
    if maior_elemento_na_linha == 0:
        print(f"Aviso: Linha {i} contém apenas zero ou o maior elemento é zero. Divisão não será possível.")
        continue 

    for j in range(len(matriz_A_original[i])):
        matriz_A_original[i][j] = matriz_A_original[i][j] / maior_elemento_na_linha


print("\nMatriz A Modificada:")
for i in range(len(matriz_A_original)):
    for j in range(len(matriz_A_original[0])):
        print(f"{matriz_A_original[i][j]:8.4f}", end="")
    print()

print("-" * 40)