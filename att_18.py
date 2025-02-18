#  18. Faça um programa que receba 10 números e apresente a soma dos números pares e 
# dos números ímpares;
soma = 0
soma1 = 0

for numero in range(1,11):
    valor = int(input('Digite um número: '))
    if valor % 2 == 0:
        print(valor)
        soma = soma + valor
    elif valor % 2 != 0:
        print(valor)
        soma1 = soma1 + valor

print(f'Valor par {soma}')
print(f'Valor impar {soma1}')