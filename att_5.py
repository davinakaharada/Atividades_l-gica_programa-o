'''
5. Faça um programa que recebe um número em Pés, faça as conversões a seguir e 
mostre os resultados.
 Polegadas;- - 
Jardas;
 Milhas;

 Sabe –se que:
 1 Pé = 12 polegadas;
 1 Jarda = 3 Pés;
 1 Milha = 1.760 Jarda;
'''
pes = float(input('Digite o valor em pés: '))

polegadas = pes * 12 
jardas = pes * 3
milhas = pes * 1.760

print(polegadas, jardas, milhas)

