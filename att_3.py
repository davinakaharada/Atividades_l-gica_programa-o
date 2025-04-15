#  3. Faça um programa que receba o salário de um funcionário, calcule e mostre o novo 
# salário, sabendo-se que este sofreu um aumento de 25%.

# salario = float(input('Digite o seu salário: '))

# aumento = salario * 1.25

# print(f'Seu salário atual será de R${aumento} reais')

def salario(salario):
    aumento = salario * 1.25
    return f'Seu salário atual será de R${aumento} reais'
print(salario(5000))