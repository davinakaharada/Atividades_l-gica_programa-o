# 44.	Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros.
# Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M.
# como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def converter_para_12h(horas_24, minutos):
  if not (0 <= horas_24 <= 23 and 0 <= minutos <= 59):
    print("Erro: Horário ou minutos inválidos. Digite valores entre 0-23 para horas e 0-59 para minutos.")
    return None

  periodo = ''
  horas_12 = horas_24

  if horas_24 == 0:
    horas_12 = 12
    periodo = 'A'
  elif 1 <= horas_24 <= 11:
    periodo = 'A'
  elif horas_24 == 12: 
    periodo = 'P'
  else: 
    horas_12 = horas_24 - 12
    periodo = 'P'

  return (horas_12, minutos, periodo)

def exibir_hora_12h(horas_12, minutos, periodo):
  
  minutos_str = f"{minutos:02d}"
  periodo_str = "A.M." if periodo == 'A' else "P.M."
  print(f"O horário convertido é: {horas_12}:{minutos_str} {periodo_str}")

def programa_conversor_horas():
  
  print("--- Conversor de Horas (24h para 12h) ---")
  while True:
    try:
      horas_input = int(input("Digite a hora (0-23): "))
      minutos_input = int(input("Digite os minutos (0-59): "))

      resultado_conversao = converter_para_12h(horas_input, minutos_input)

      if resultado_conversao: 
        horas_12, minutos, periodo = resultado_conversao
        exibir_hora_12h(horas_12, minutos, periodo)

    except ValueError:
      print("Entrada inválida. Por favor, digite números inteiros para horas e minutos.")
    except Exception as e:
      print(f"Ocorreu um erro inesperado: {e}")

    continuar = input("\nDeseja converter outro horário? (s/n): ").strip().lower()
    if continuar != 's':
      print("Obrigado por usar o conversor de horas!")
      break

if __name__ == "__main__":
  programa_conversor_horas()