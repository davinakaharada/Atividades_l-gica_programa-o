# 12. Escreva um algoritmo que a partir da massa e da altura informados pelo usuário, 
# calcule e apresente seu IMC e sua classificação conforme a tabela abaixo:
#  IMC Classificação
#  < 18 Magreza
#  18 ~ 24,9 Saudável
#  25 ~ 29,9 Sobrepeso
#  >= 30 Obesidade

peso = int(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

calcula_imc = peso / altura**2

if calcula_imc < 18:
    print(f'O seu IMC é {calcula_imc} você está muito magro!')
elif calcula_imc >=18 and calcula_imc <= 24.9:
    print(f'O seu IMC é {calcula_imc} você está saudável')
elif calcula_imc >= 25 and calcula_imc <= 29.9:
    print(f'O seu IMC pe {calcula_imc} você está com sobrepeso')
else:
    print(f'O seu IMC è {calcula_imc} você está obeso')
