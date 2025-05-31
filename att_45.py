# 45.	Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA.
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

from datetime import datetime

def converter_data_por_extenso(data_str):
  meses_por_extenso = {
      1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
      5: "maio", 6: "junho", 7: "julho", 8: "agosto",
      9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
  }

  try:
    data_obj = datetime.strptime(data_str, "%d/%m/%Y")

    dia = data_obj.day
    mes_numero = data_obj.month
    ano = data_obj.year

    mes_extenso = meses_por_extenso.get(mes_numero)

    if mes_extenso:
      return f"{dia} de {mes_extenso} de {ano}"
    else:
      return None

  except ValueError:
    return None

print(f"25/12/2023 -> {converter_data_por_extenso('25/12/2023')}")
print(f"01/01/2024 -> {converter_data_por_extenso('01/01/2024')}")
print(f"15/05/2025 -> {converter_data_por_extenso('15/05/2025')}") 
print(f"08/03/1990 -> {converter_data_por_extenso('08/03/1990')}")
