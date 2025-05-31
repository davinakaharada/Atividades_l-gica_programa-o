# 34.	Ler uma matriz D 5 x 5 (considere que não serão informados valores duplicados).
# A seguir ler um número X e escreva uma mensagem indicando se o valor de X existe ou NÃO na matriz.

print("--- Exercício 34: Verificar Número na Matriz ---")

matriz_D = [
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]


print("\nMatriz D (5x5):")
for i in range(5):
    for j in range(5):
        print(f"{matriz_D[i][j]:4}", end="")
    print()

numero_X = 0
while True:
    try:
        numero_X = int(input("\nDigite um número para buscar na matriz: "))
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")


encontrado = False

for i in range(5): 
    for j in range(5): 
        if matriz_D[i][j] == numero_X:
            encontrado = True 
            pass 


if encontrado:
    print(f"O valor {numero_X} EXISTE na matriz.")
else:
    print(f"O valor {numero_X} NÃO existe na matriz.")

print("-" * 40)