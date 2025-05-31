# 40.	Refaça a lógica anterior, porém para a multiplicação deve ser feita utilizando seguidas somas.

def adicionar(num1, num2):
  return num1 + num2

def subtrair(num1, num2):
  return num1 - num2

def multiplicar_por_somas(num1, num2):
  if num1 == 0 or num2 == 0:
    return 0

  resultado = 0
  
  sinal_negativo = (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0)

  
  abs_num1 = abs(num1)
  abs_num2 = abs(num2)

  
  for _ in range(int(abs_num2)): 
    resultado = adicionar(resultado, abs_num1)


  if sinal_negativo:
    return -resultado
  else:
    return resultado

def dividir(num1, num2):
  if num2 == 0:
    return "Erro: Não dá pra dividir por zero!"
  return num1 / num2

def calculadora_simples():
  print("--- Calculadora Simples (Multiplicação por Somas) ---")

  try:
    valor1 = float(input("Digite o primeiro número: "))
    valor2 = float(input("Digite o segundo número: "))
  except ValueError:
    print("Ops! Por favor, digite apenas números válidos.")
    return

  operacao = input("Qual operação você quer? (+, -, *, /): ").strip()

  resultado = None
  if operacao == '+':
    resultado = adicionar(valor1, valor2)
  elif operacao == '-':
    resultado = subtrair(valor1, valor2)
  elif operacao == '*':
  
    resultado = multiplicar_por_somas(valor1, valor2)
  elif operacao == '/':
    resultado = dividir(valor1, valor2)
  else:
    print("Operação inválida. Tente novamente com +, -, * ou /.")

  if resultado is not None:
    print(f"O resultado é: {resultado}")


if __name__ == "__main__":
  calculadora_simples()