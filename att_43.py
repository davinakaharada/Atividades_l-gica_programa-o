# 43.	Organiza número. Faça uma rotina que organize os números recebidos em: crescente, decrescente e reverso. 
# Por exemplo:  
# recebido: 293
# •	crescente: 239
# •	decrescente: 932
# •	reverso: 392

def organizar_numero(numero_recebido):

  str_numero = str(numero_recebido)

  lista_digitos = sorted(list(str_numero)) 

  crescente = "".join(lista_digitos)

  decrescente = "".join(sorted(lista_digitos, reverse=True))

  reverso = str_numero[::-1]
  return {
      "original": numero_recebido,
      "crescente": int(crescente),
      "decrescente": int(decrescente),
      "reverso": int(reverso)
  }


numero1 = 293
resultado1 = organizar_numero(numero1)
print(f"Recebido: {resultado1['original']}")
print(f"  Crescente: {resultado1['crescente']}")
print(f"  Decrescente: {resultado1['decrescente']}")
print(f"  Reverso: {resultado1['reverso']}\n")
