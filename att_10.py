# 10. Escreva um programa que leia a velocidade máxima permitida em uma avenida e 
# velocidade com que o motorista estava dirigindo nela e calcule a multa que uma 
# pessoa vai receber;
# Até 10 km/h R$ 50,00
# 11 a 30 km/h R$ 100,00
# Mais 31 km/h R$ 200,00
#Exemplo: 
# Limite: 50 km/h
# Velocidade: 59 km/h
# Multa: R$ 50,00

velocidade_permitida = 50
while True:
    velocidade_ultrapassada = int(input('Digite a sua velocidade atual: '))

    if velocidade_ultrapassada <= 50:
        print('A velocidade está de acordo com o permitido')
    elif velocidade_ultrapassada > velocidade_permitida and velocidade_ultrapassada<= (velocidade_permitida*1.20):
        print(f'A velocidade está em {velocidade_ultrapassada} km, você levou uma multa de R$50,00 reais')
    elif velocidade_ultrapassada>(velocidade_permitida*1.20) and velocidade_ultrapassada<=(velocidade_permitida*1.60):
        print(f'A velocidade está em {velocidade_ultrapassada} km, você levou uma multa de R$100,00 reais')
    else:
        print(f'A velocidade está em {velocidade_ultrapassada} km, você levou uma multa de R$200,00 reais')

        
