# 41.	Defina uma função chamada velocidade_media() em um script que recebe dois parâmetros: a distância percorrida (em metros) e o tempo (em segundos) gasto.

def velocidade_media(distancia, tempo):
  
  if tempo <= 0:
    return 
  
  velocidade = distancia / tempo
  return f'A velocidade média foi de {velocidade:.2f} m/s'


print(velocidade_media(350, 90)) 
print(velocidade_media(1000, 60)) 
print(velocidade_media(500, 0))   