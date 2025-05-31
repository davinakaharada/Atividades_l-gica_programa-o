# 38.	Logo após, ler uma matriz 13 x 3 que contenha a aposta de um jogador.
# Considere que cada posição da matriz armazenará o valor 1 se for apostado, 0 caso contrário.
#  Calcular e escrever o número de pontos obtidos pelo jogador. Escrever também o número de apostas simples, dupla ou tripla utilizadas pelo apostador.

print("--- Exercício 38: Conferir Aposta do Jogador ---")


vetor_Gabarito = [1, 2, 1, 3, 1, 2, 3, 1, 2, 1, 3, 2, 1]

matriz_Aposta = [
    [1, 0, 0], 
    [0, 1, 0], 
    [1, 1, 0], 
    [0, 0, 1], 
    [0, 1, 0], 
    [1, 1, 0], 
    [1, 1, 1], 
    [1, 0, 0], 
    [0, 0, 1], 
    [1, 0, 0], 
    [1, 1, 0], 
    [0, 1, 0], 
    [0, 0, 1]  
]

NUM_JOGOS = 13
NUM_COLUNAS_APOSTA = 3

total_pontos = 0
apostas_simples = 0
apostas_duplas = 0
apostas_triplas = 0

print("\n--- Gabarito ---")
for i in range(NUM_JOGOS):
    print(f"Jogo {i+1}: {vetor_Gabarito[i]}")

print("\n--- Aposta do Jogador ---")
for i in range(NUM_JOGOS):
    print(f"Jogo {i+1}: ", end="")
    for j in range(NUM_COLUNAS_APOSTA):
        print(f"{matriz_Aposta[i][j]} ", end="")
    print()

print("\n--- Conferindo Aposta ---")

for i in range(NUM_JOGOS): 
    aposta_no_jogo = matriz_Aposta[i]
    gabarito_do_jogo = vetor_Gabarito[i]

    soma_apostas_na_linha = aposta_no_jogo[0] + aposta_no_jogo[1] + aposta_no_jogo[2]
    if soma_apostas_na_linha == 1:
        apostas_simples = apostas_simples + 1
    elif soma_apostas_na_linha == 2:
        apostas_duplas = apostas_duplas + 1
    elif soma_apostas_na_linha == 3:
        apostas_triplas = apostas_triplas + 1


    acertou_jogo = False
    if gabarito_do_jogo == 1:
        if aposta_no_jogo[0] == 1: 
            acertou_jogo = True
    elif gabarito_do_jogo == 2: 
        if aposta_no_jogo[1] == 1: 
            acertou_jogo = True
    elif gabarito_do_jogo == 3: 
        if aposta_no_jogo[2] == 1: 
            acertou_jogo = True

    if acertou_jogo:
        total_pontos = total_pontos + 1
        print(f"Jogo {i+1}: ACERTOU!")
    else:
        print(f"Jogo {i+1}: Errou.")

print(f"\nTotal de pontos obtidos pelo jogador: {total_pontos}")
print(f"Número de apostas simples: {apostas_simples}")
print(f"Número de apostas duplas: {apostas_duplas}")
print(f"Número de apostas triplas: {apostas_triplas}")

print("-" * 40)