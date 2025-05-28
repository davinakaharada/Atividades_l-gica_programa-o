


def fibonacci_n(n):
    if n <= 0:
        return "Posição inválida. Use um número maior que 0."
    elif n == 1 or n == 2:
        return 1

    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

n = int(input("Digite a posição n da sequência de Fibonacci: "))
resultado = fibonacci_n(n)
print(f"O {n}º número da sequência de Fibonacci é {resultado}")
