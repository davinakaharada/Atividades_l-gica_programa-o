#  15. Faça um programa que calcule a tabuada de um número digitado pelo usuário

numero_tabuada = int(input('Digite um valor: '))

for i in range(1,11):
    print(f'{numero_tabuada} X {i} = {numero_tabuada * i}')