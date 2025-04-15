#  9. Faça um programa para exibir a ocupação de um funcionário a partir de seu código 
# de profissão, de acordo com a tabela abaixo;
#  1 Matemático
# 2 Analista de Sistemas
# 3 Físico
# 4 Arquiteto
# 5 Piloto de Aeronaves
# codigo_profissao = {
#         '1' : 'Matemático',
#         '2' : 'Analista de Sistemas',
#         '3' : 'Físico',
#         '4' : 'Arquiteto',
#         '5' : 'Piloto de Aeronaves'
#     }


# while True: 
#     ocupacao = input('Digite o código da profissão: ')

#     print(codigo_profissao[ocupacao])

    

codigo_profissao = {
        '1' : 'Matemático',
        '2' : 'Analista de Sistemas',
        '3' : 'Físico',
        '4' : 'Arquiteto',
        '5' : 'Piloto de Aeronaves'
    }

def exibir_ocupacao(ocupacao):
    return codigo_profissao[ocupacao]
print(exibir_ocupacao('2'))