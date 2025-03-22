#  21. Faça um programa que receba 10 números, calcule e mostre:
#   A soma dos números digitados;
#   A quantidade de números digitados;
#   A média dos números digitados;
#   O maior número digitado;  
#  O menor número digitado;
#   A média dos números pares;
#   A porcentagem dos números ímpares entre todos os números digitados. 
# Finalize a entrada de dados com a digitação do número 30.000.

lista = []

for numeros in range(10):
    valor = int(input('Digite 10 valores inteiros: '))
    if valor == 30000:
        break
    lista.append(valor)

quantidade = len(lista)
soma_valores = sum(lista)
media_valores = soma_valores / quantidade if quantidade > 0 else 0
maior_valor = max(lista) if quantidade > 0 else None
menor_valor = min(lista) if quantidade > 0 else None

pares = [num for num in lista if num % 2 == 0]
media_pares = sum(pares) / len(pares) if len(pares) > 0 else 0

impares = [num for num in lista if num % 2 != 0]
porcentagem_impares = (len(impares) / quantidade * 100) if quantidade > 0 else 0

print(f"Soma dos valores: {soma_valores}")
print(f"Quantidade de números digitados: {quantidade}")
print(f"Média dos valores: {media_valores:.2f}")
print(f"Maior valor: {maior_valor}")
print(f"Menor valor: {menor_valor}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Porcentagem de números ímpares: {porcentagem_impares:.2f}%")
