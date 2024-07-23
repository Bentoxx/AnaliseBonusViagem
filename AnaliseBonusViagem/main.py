import pandas as pd
#Passo a passo da aplicação

#Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    print (mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    print (tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any():
        print ('Encontrou alguém com vendas acima de R$ 55.000,00')
#Para cada arquivo:

#Verificar se algum valor da coluna de vendas > R$ 55.000,00

#Se > R$ 55.000,00 -> enviar um SMS com o nome do vendedor, o mês e o valor de vendido
