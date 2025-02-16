#  6. Faça um programa que receba o salário de um funcionário, calcule e mostre o novo 
# salário, sabendo-se que:
# Salário < R$ 1000,00 aumento de 25%.
# Salário >= R$ 1000,00 e < R$ 2000,00 aumento de 15%.
# Salário >= R$ 2000,00 aumento de 10%.

salario = float(input('Digite o seu salário: '))

if salario < 1000:
    print(f'seu aumento é de 25%. Seu salário atual será de {salario*1.25}')
elif salario >= 1000 and salario < 2000:
    print(f'seu aumento é de 15%. Seu salário atual será de {salario*1.15}')
else:
    print(f'seu aumento é de 10%. Seu salário atual será de {salario*1.10}')