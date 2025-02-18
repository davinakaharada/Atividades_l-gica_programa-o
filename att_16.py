#  16. Faça um programa que calcula a tabuada dos números 2 a 9

for tabuada in range(2,10):
    for numero in range(1,11):
        resultado = tabuada * numero
        print(f'{tabuada} X {numero} = {resultado}')