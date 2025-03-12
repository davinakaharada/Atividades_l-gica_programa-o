# 19. Faça um programa que receba duas notas de seis alunos. Calcule e mostre:
# A média aritmética das duas notas de cada aluno; e
#A mensagem que está na tabela a seguir:
#        Média Aritmética | Mensagem
#        Até 3            | Reprovado
#        Entre 3 e 7      | Exame
#        De 7 para cima   | Aprovado
# O total de alunos aprovados;
# O total de alunos de exame;
# O total de alunos reprovados;
# A média da classe.

contAlunos = 1
qtdAlunos = 3
qtdNotas = 2
qtdAprovados = 0
qtdReprovados = 0
qtdExame = 0
somaMedias = 0

while contAlunos <= qtdAlunos:
    print('\n')
    print('#####################')
    print(f'Aluno {contAlunos}')

    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))
    media = (nota1 + nota2) / qtdNotas
    somaMedias += media
    contAlunos +=1

    if media < 3:
        print('Reprovado')
        qtdReprovados += 1
    elif media >=3 and media < 7:
        print('Exame')
        qtdExame += 1
    elif media >=7:
        print('Aprovado')
        qtdAprovados += 1

mediaCLasse = somaMedias / qtdAlunos
print('\n')
print(f'Aprovados {qtdAprovados}')
print('\n')
print(f'exame {qtdExame}')
print('\n')
print(f'Reprovados {qtdReprovados}')
print('\n')
print(f'Média {somaMedias}')
