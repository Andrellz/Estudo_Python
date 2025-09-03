''' Exercício sobre preparação de dados ---- Flores'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

caminho_do_csv_para_analise = r"C:\Users\andre\Downloads\iris.csv"

dataset = pd.read_csv(caminho_do_csv_para_analise)

dataset.columns = ['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth', 'class']

print(dataset.head(10))

print(dataset.shape)

#Então são 150 colunas

#mostrando os 5 ultimos:

print(dataset.tail())

print(dataset.info())

print(dataset.dtypes)

print(dataset[(dataset.sepalLength == 4.7)])