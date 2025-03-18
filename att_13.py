#  13. Faça um programa que receba 3 valores e verifique se eles podem representar os 
# lados em um triângulo;
#  Nome Característica
#  Equilátero 3 lados iguais
#  Isósceles 2 lados iguais
# Escaleno
#  3 lados diferente
#  Lembre-se que para formar um triângulo, nenhum dos lados pode ser igual a zero e 
# cada um dos lados precisa ser menor que a soma dos outros dois

lista = []

for i in range(3):
    valor = int(input(f'Digite o {i+1}º valor: '))
    lista.append(valor)

a, b, c = lista

if a <= 0 or b <= 0 or c <= 0:
    print("Os lados não podem ser zero ou negativos.")
elif a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Triângulo Equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Os valores informados não formam um triângulo.")
