# 27.	Elabore um programa que receba a base e o expoente e, utilizando laços e multiplicação, apresente o valor da potência gerada.


base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente (positivo): "))

resultado = 1

for _ in range(expoente):
    resultado *= base

print(f"{base} elevado a {expoente} é igual a {resultado}")
