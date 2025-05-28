# 28.Refaça o exercício anterior, porém agora substitua a multiplicação pela soma. (Entende-se que: 3 x 3 = 3 + 3 + 3)


def multiplicar(a, b):
    resultado = 0
    for _ in range(b):
        resultado += a
    return resultado


def potencia(base, expoente):
    resultado = 1
    for _ in range(expoente):
        resultado = multiplicar(resultado, base)
    return resultado

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente (positivo): "))

resultado = potencia(base, expoente)
print(f"{base} elevado a {expoente} é igual a {resultado}")
