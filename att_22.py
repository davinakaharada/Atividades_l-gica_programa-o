    #  22. Um funcionário de uma empresa recebe, anualmente, aumento salarial. Sabe-se que:
    #  a. Esse funcionário foi contratado em 2005, com salário inicial de R$ 1000,00;
    #  b. Em 2006, ele recebeu aumento de 1,5% sobre seu salário inicial.
    #  c. A partir de 2007 (inclusive), os aumentos salariais sempre corresponderam ao dobro 
    # do percentual do ano anterior.
    #  Faça um programa que determine o salário atual desse funcionário.

ano_contratacao = 2005
salario_inicial = 1000.00
percentual_aumento = 1.5 / 100
ano_atual = 2025  

salario = salario_inicial

for ano in range(2006, ano_atual + 1):
    aumento = salario * percentual_aumento
    salario += aumento
    percentual_aumento *= 2  

print(f"O salário do funcionário em {ano_atual} é: R$ {salario:.2f}")