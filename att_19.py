#  19. Faça um programa que receba duas notas de seis alunos. Calcule e mostre:
#   A média aritmética das duas notas de cada aluno; e
#   A mensagem que está na tabela a seguir:
#  Média Aritmética
#  Até 3
#  Entre 3 e 7 
# Mensagem
#  Reprovado 
# Exame
#  De 7 para cima
#   O total de alunos aprovados;
#   O total de alunos de exame;
#   O total de alunos reprovados;
#   A média da classe.


medias = []
aprovado = 0
reprovado = 0
exame = 0

for i in range(6):
    print(f"\nAluno {i+1}")
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    
    media = (n1 + n2) / 2
    medias.append(media)

    print(f"Média: {media:.2f}")
    
    if media <= 3:
        print('Situação: Reprovado')
        reprovado += 1
    elif media <= 7:
        print('Situação: Exame')
        exame += 1
    else:
        print('Situação: Aprovado')
        aprovado += 1

# Cálculo da média da classe
media_classe = sum(medias) / len(medias)

# Resultados finais
print("\nResumo Final:")
print(f'Total de aprovados: {aprovado}')
print(f'Total de exames: {exame}')
print(f'Total de reprovados: {reprovado}')
print(f'Média da classe: {media_classe:.2f}')

    


