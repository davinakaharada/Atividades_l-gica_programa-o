# 39. Crie uma rotina de calculadora, onde receba dois valores e indique e receba qual operação básica deseja calcular, em seguida apresente o resultado.
# Todo o cálculo deve ser feito com uso de funções.

def adicionar(num1, num2):
  return num1 + num2

def subtrair(num1, num2):
  return num1 - num2

def multiplicar(num1, num2):
  return num1 * num2

def dividir(num1, num2):
  if num2 == 0:
    return "Erro: Não dá pra dividir por zero!"
  return num1 / num2

def calculadora_simples():
  print("--- Calculadora Simples ---")

  # Pede os dois números
  try:
    val1 = float(input("Digite o primeiro número: "))
    val2 = float(input("Digite o segundo número: "))
  except ValueError:
    print("Ops! Por favor, digite apenas números válidos.")
    return 

  
  operacao = input("Qual operação você quer? (+, -, *, /): ").strip()

  resultado = None
  if operacao == '+':
    resultado = adicionar(val1, val2)
  elif operacao == '-':
    resultado = subtrair(val1, val2)
  elif operacao == '*':
    resultado = multiplicar(val1, val2)
  elif operacao == '/':
    resultado = dividir(val1, val2)
  else:
    print("Operação inválida. Tente novamente com +, -, * ou /.")

  
  if resultado is not None:
    print(f"O resultado é: {resultado}")


if __name__ == "__main__":
  calculadora_simples()
