# 37.	Ler um vetor G de 13 elementos que contenha o gabarito da loteria esportiva codificado da seguinte forma: 1-coluna um, 2-coluna do meio, 3-coluna dois.

print("--- Exercício 37: Gabarito da Loteria Esportiva ---")


vetor_G = [1, 2, 1, 3, 1, 2, 3, 1, 2, 1, 3, 2, 1]

print("\nGabarito da Loteria Esportiva (Vetor G):")
for i in range(len(vetor_G)):
    print(f"Jogo {i+1}: {vetor_G[i]}")

print("\nInterpretação do Gabarito:")
for i in range(len(vetor_G)):
    resultado_jogo = vetor_G[i]
    mensagem_resultado = ""

    if resultado_jogo == 1:
        mensagem_resultado = "Coluna um"
    elif resultado_jogo == 2:
        mensagem_resultado = "Coluna do meio"
    elif resultado_jogo == 3:
        mensagem_resultado = "Coluna dois"
    else:
        mensagem_resultado = "Valor inválido no gabarito" # Para tratar caso haja erro

    print(f"Jogo {i+1}: {mensagem_resultado}")

print("-" * 40)