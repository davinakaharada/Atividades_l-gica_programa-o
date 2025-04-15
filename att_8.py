# 8. Escreva um programa que leia a idade de um indivíduo e escreva a faixa etária a que 
#pertence, de acordo com a tabela abaixo;
# Faixa etária
# < 12 criança
# 13 a 17 adolescente
# 18 a 59 adulto
# maior de 60 especialista

nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))

if idade > 0 and idade < 12:
    print(f'{nome} tem {idade} anos e é criança')
elif idade >= 13 and idade <=17:
    print(f'{nome} tem {idade} anos e é adolescente')
elif idade >=18 and idade <= 59:
    print(f'{nome} tem {idade} anos e é adulto')
else:
    print(f'{nome} tem {idade} anos e é idoso')