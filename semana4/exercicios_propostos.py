'''exercícios do 1 ao 6'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



caminho_do_csv_para_analise = r"C:\Users\andre\Downloads\sales_data.csv"

dataset = pd.read_csv(caminho_do_csv_para_analise)


# print(dataset.columns)
# print(dataset.info())

# print(dataset['Region'].unique())

# print(dataset.describe(include='all'))


#Questão - ilustrar os dados por meio de gráficos

# print(dataset['Region'].unique())

categorias = dataset['Region'].unique()
valores = dataset['Inventory Level'].sum()

plt.bar(categorias, valores, color='skyblue')

plt.title('Exemplo de Gráfico de Barras')
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.plot()
# plt.show()

print(valores)

#assim podemos ver um maior ocasionamento de região Norte

#print(dataset.columns)

#vamos ver qual produto apresenta menor inventário, bom para já planejar a proxima compra

produto_menor_inventório = dataset[['Product ID', 'Inventory Level']]


#print(produto_menor_inventório.max(), produto_menor_inventório.min())

#Assim, vemos que ter itens que não estão presentes no inventório, mas neste caso é coerente
# Quais itens estão com quantidade 0 no inventório?

#print(dataset['Inventory Level'].isnull().value_counts())

print(dataset.iloc[0])

print(dataset.columns)

# print(dataset.describe())


#quais itens estão acabando ou já acabaram
#qual o percentual em relação ao competidor
#qual o produtor que o concorrente tem que é bem mais barato



# print(dataset.columns)

'''Index(['Date', 'Store ID', 'Product ID', 'Category', 'Region',
       'Inventory Level', 'Units Sold', 'Units Ordered', 'Price', 'Discount',
       'Weather Condition', 'Promotion', 'Competitor Pricing', 'Seasonality',
       'Epidemic', 'Demand'],  '''

condicao = dataset['Inventory Level'] ==0
condicao2 = dataset['Product ID'] =='P0016'

# print(dataset[condicao][['Product ID','Inventory Level']].value_counts())

print(dataset[condicao2][['Region','Store ID','Product ID','Inventory Level']])


#Assim é possivel observar que um mesmo item pode se repetir para uma mesma região e mesmo store ID, e estando em falta, o que é um pouco estranho
#como já tem o valor zero alterarei de outro modo não sendo o fillna

dataset[dataset['Inventory Level'] ==0]= dataset['Inventory Level'].mean()

plt.bar(categorias, valores, color='skyblue')

plt.title('Exemplo de Gráfico de Barras')
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.plot()
plt.show()