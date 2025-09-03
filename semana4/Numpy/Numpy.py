import pandas as pd


data = pd.read_csv("C:/Users/andre/Downloads/archive/2004-2021.tsv", sep='\t')
data['PREÇO MÍNIMO DISTRIBUIÇÃO'] = pd.to_numeric(
    data['PREÇO MÍNIMO DISTRIBUIÇÃO'],
    errors='coerce')

teste = data['PREÇO MÍNIMO DISTRIBUIÇÃO'].max

lista_anos = ['2020, 2022, 2021']

#selecao.teste = data.query('Ano in @lista_anos')


#print(selecao.teste)




#Limpeza de dados

#procurando se tem dados vazios


#por meio desta função podemos ver se tem valores nulos ou não

#nan é not a number



#print(data.info('DATA FINAL'))

for atributo in ['NÚMERO DE POSTOS PESQUISADOS', 'PREÇO MÉDIO REVENDA', 'DESVIO PADRÃO REVENDA', 'PREÇO MÍNIMO REVENDA', 'PREÇO MÁXIMO REVENDA', 'COEF DE VARIAÇÃO REVENDA', 'PREÇO MÍNIMO DISTRIBUIÇÃO']:
    data[atributo] = pd.to_numeric(data[atributo], errors='coerce')

mask = data['PREÇO MÍNIMO DISTRIBUIÇÃO'].isnull()
data.dropna(inplace= True)

#print(data['PREÇO MÉDIO REVENDA'].mean())

#print(f'A média dos precos é {data['PREÇO MÉDIO REVENDA'].mean():.2f}')

#print(data['REGIÃO'].unique())

#print(data['REGIÃO'].value_counts().to_frame())

dados_vendas = {
    'Nome do Vendedor': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Erica'],
    'Região': ['Norte', 'Sul', 'Centro', 'Norte', 'Sul'],
    'Vendas Mensais (R$)': [15000, 22500, 18000, 15000, 25000],
    'Avaliação (1-5)': [4, 5, 3, 4, 5],
    'Status': ['Ativo', 'Ativo', 'Férias', 'Ativo', 'Ativo']
}


dt = pd.DataFrame(dados_vendas)
print(dt.head())


