# 23.	Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e sua opinião em relação ao filme:
# Ótimo – 3;  2 – Bom;  1 – Regular. Faça um programa que receba a idade e a opinião de 15 espectadores, calcule e mostre:
# 	A média da idade das pessoas que responderam ótimo;
# 	A quantidade de pessoas que responderam regular;
# 	A porcentagem de pessoas que responderam Bom, entre todos os espectadores analisados. 

# Inicialização de variáveis
soma_idade_otimo = 0
qtde_otimo = 0
qtde_regular = 0
qtde_bom = 0
total_espectadores = 15


for i in range(total_espectadores):
    print(f"\nEspectador {i+1}")
    idade = int(input("Digite a idade: "))
    opiniao = int(input("Opinião sobre o filme (3-Ótimo, 2-Bom, 1-Regular): "))

    if opiniao == 3:
        soma_idade_otimo += idade
        qtde_otimo += 1
    elif opiniao == 2:
        qtde_bom += 1
    elif opiniao == 1:
        qtde_regular += 1
    else:
        print("Opinião inválida! Ignorando este dado.")

if qtde_otimo > 0:
    media_idade_otimo = soma_idade_otimo / qtde_otimo
else:
    media_idade_otimo = 0

porcentagem_bom = (qtde_bom / total_espectadores) * 100

print("\nResultados finais:")
print(f"Média de idade dos que responderam 'Ótimo': {media_idade_otimo:.2f}")
print(f"Quantidade de pessoas que responderam 'Regular': {qtde_regular}")
print(f"Porcentagem de pessoas que responderam 'Bom': {porcentagem_bom:.2f}%")
