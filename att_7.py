#  7. Faça um programa que receba o mês em número e apresente-o por extenso.

# meses = ['Janeiro','Fevereiro','Março','Abril', 'Maio','Junho',
#          'Julho','Agosto','Setembro','Outrubo','Novembro','Dezembro']

# mes_numero = int(input('Digite o mês em número: '))

# if mes_numero > 0 and mes_numero <= 12:
#     print(f"O mês correspondente é {meses[mes_numero - 1]}")


meses = ['Janeiro','Fevereiro','Março','Abril', 'Maio','Junho',
         'Julho','Agosto','Setembro','Outrubo','Novembro','Dezembro']

def mes_numero(mes_numero):
    if mes_numero > 0 and mes_numero <= 12:
        return f'O mês correspondente é {meses[mes_numero - 1]}'
    
print(mes_numero(3))