# 25.	Abaixo temos a famosa sequência.

# 1, 1, 2, 3, 5, 8, 13, 21, 34....
# Encontre a lógica utilizada nesta parte de sequência e desenvolva um algoritmo capaz de reproduzir as 30 primeiras ocorrências desta sequência. 


# Gerar os 30 primeiros números da sequência de Fibonacci

fibonacci = [1, 1]  # Início da sequência

while len(fibonacci) < 30:
    proximo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo)

# Exibir a sequência
for i, num in enumerate(fibonacci, 1):
    print(f"{i}: {num}")
