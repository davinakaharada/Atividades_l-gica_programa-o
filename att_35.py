# 35.	Ler uma matriz G 5 x 5 e criar 2 vetores SL e SC de 5 elementos que contenham respectivamente as somas das linhas e das colunas de G.
# Escrever os vetores criados.

print("--- Exercício 35: Somar Linhas e Colunas da Matriz G ---")

matriz_G = [
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5]
]

print("\nMatriz G (5x5):")
for i in range(5):
    for j in range(5):
        print(f"{matriz_G[i][j]:4}", end="")
    print()

vetor_SL = [0, 0, 0, 0, 0] 
vetor_SC = [0, 0, 0, 0, 0] 


for i in range(5): 
    soma_linha_atual = 0
    for j in range(5): 
        soma_linha_atual = soma_linha_atual + matriz_G[i][j]
    vetor_SL[i] = soma_linha_atual 

for j in range(5): 
    soma_coluna_atual = 0
    for i in range(5): 
        soma_coluna_atual = soma_coluna_atual + matriz_G[i][j]
    vetor_SC[j] = soma_coluna_atual 


print("\nVetor SL (Soma das Linhas):")

for i in range(len(vetor_SL)):
    print(f"{vetor_SL[i]} ", end="")
print() 

print("\nVetor SC (Soma das Colunas):")
for i in range(len(vetor_SC)):
    print(f"{vetor_SC[i]} ", end="")
print() 

print("-" * 40)