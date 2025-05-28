# 17.Faça um programa que receba dois valores, sendo que o primeiro deve ser menor que o segundo.
# O programa deve apresentar todos os números ímpares contidos nesta sequência. (Modulo %. Exemplo: 7%2 = 1)


inicio = int(input("Digite o primeiro valor (menor): "))
fim = int(input("Digite o segundo valor (maior): "))


if inicio >= fim:
    print("Erro: o primeiro valor deve ser menor que o segundo.")
else:
    print("Números ímpares entre", inicio, "e", fim, ":")
    for numero in range(inicio + 1, fim):  
        if numero % 2 != 0:
            print(numero)
