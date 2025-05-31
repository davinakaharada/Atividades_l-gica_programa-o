# 30. Um alpinista deve subir uma montanha. O percurso terá 2500 metros. Cada passo do
# alpinista, morro acima, tem 47 centímetros, porém a cada 10 passo ele escorrega 1.
# Para atingir seu objetivo, quantos passos o alpinista dará? (Resolva fazendo um
# programa que utilize laços para solucionar o problema).


altura_montanha_cm = 2500 * 100  
passo_cm = 47
deslize_cm = passo_cm  
passos_totais = 0
distancia_percorrida = 0


while distancia_percorrida < altura_montanha_cm:
    for _ in range(10): 
        if distancia_percorrida < altura_montanha_cm:
            distancia_percorrida += passo_cm
            passos_totais += 1

    
    if distancia_percorrida < altura_montanha_cm:
        distancia_percorrida -= deslize_cm


print(f"O alpinista dará {passos_totais} passos para atingir o topo da montanha.")
