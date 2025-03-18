#  11. Escreva um algoritmo para exibir o nome do lanche a partir da entrada do número do 
# mesmo pelo usuário, de acordo com a tabela abaixo:
#  Nr. Lanche
#  1 Big Mac
#  2 Quarteirão
#  3 McChicken
#  4 Cheddar McMelt
#  5 McMax

lanches = {
    '1' : 'Big Mac',
    '2' : 'Quarteirão',
    '3' : 'McChiken',
    '4' : 'Cheddar McMelt',
    '5' : 'McMax'
}

while True:
    numero = input('Digite o número do lanche: ')

    print(lanches[numero])