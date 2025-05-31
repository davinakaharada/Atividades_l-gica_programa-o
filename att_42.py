# 42.	Utilizando a lógica anterior modifique a função velocidade_media() utilizando uma função divisao() para calcular a velocidade.
# A função divisao() recebe dois números como parâmetros, calcula e retorna o resultado da divisão do primeiro pelo segundo.

def divisao(num1, num2):
  
  if num2 == 0:
    return "Erro: Não dá pra dividir por zero!"
  return num1 / num2

def velocidade_media(distancia, tempo):
 
  if tempo <= 0:
    return "Erro: O tempo deve ser maior que zero para calcular a velocidade."


  velocidade = divisao(distancia, tempo)


  if isinstance(velocidade, str) and "Erro" in velocidade:
    return velocidade 
  else:
    return f'A velocidade média foi de {velocidade:.2f} m/s'


print(velocidade_media(350, 90)) 
print(velocidade_media(1000, 60)) 
print(velocidade_media(500, 0))   
print(velocidade_media(0, 10))    