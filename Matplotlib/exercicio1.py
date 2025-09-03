"""Exercício 1"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

caminho_do_csv_para_analise = r"C:\Users\andre\Downloads\classification_results_trial_0001.csv"

arquivo = pd.read_csv(caminho_do_csv_para_analise)

data = pd.DataFrame(arquivo)

#print(data.info)

#vendo as informações, é possivel ver que trata-se de uma eschema 100x5

#print(data.columns)

#temos aqui as seguintes colunas:'image_path', 'real_class', 'predicted_class', 'prob_benign ,'prob_malign'

# É buscado um gráfico de barras mostrando a contagem de imagens para real_class (quantas "benigno" e "maligno" são na realidade).

#é tipo assim, para quantos malignos são malignos e benignos
#para quantos benignos são malignos e benignos mesmo

# é um gráfico de barra que tem a quantidade de benigno em uma barra com benigno(verdadeiro) e quantos foram dados como malignos para este caso
#tipo, primeiro um barra para o benigno e do lado uma barra para o predicted como benigno
#na verdade primeiro tenho que transformas as colunas em eixos

barra_reais = data['real_class']
barra_predicao_negativa =data['predicted_class']

#o primeiro acredito que tá certo, mas o segundo tá estranho

#print(barra_reais)

#tá certo, mas tá faltando um count == .value_counts()  


#print(barra_reais.value_counts("malign"))   

#desse jeito é massa que mostra o percentual, bem maneiro, assim podemos ver que tem mais malignos que benignos, treta

#print(data['real_class'].value_counts())

# tbm tem como usar uma condição

condicao = data['real_class'] == 'malign'

#print(data[condicao])

#aqui temos só os malignos reais, bem legal
#tem como fazer duas condições ao mesmo tempo e daí retirar os dados para o gráfico

condicao2 = (data['real_class'] == 'malign') & (data['predicted_class'] == 'malign')

#print(data[condicao2])

#agora é pegar o raciocinio para usar nos dados, mas está promissor

nova_data = data[condicao2]

barra_real_negativo = nova_data['real_class'].value_counts()
barra_predita_negativo = nova_data['predicted_class'].value_counts()

#print(barra_real_negativo, barra_predita_negativo)

#então são 46 dados que são malignos malignos
#ainda tem os malignos com benignos e os benignos com benignos e os benignos com malignos
#entendi errado é mais simples do que imaginava, mas só comentar o que fiz para refazer da forma solicitada


condicao_real_maligna = data["real_class"] == "malign"

condicao_real_benigna = data["real_class"] == "benign"

quantidade_maligna =  data[condicao_real_maligna]
quantidade_benigna =  data[condicao_real_benigna]

teste = quantidade_maligna['real_class'].value_counts()
teste2 = quantidade_benigna['real_class'].value_counts()

#plt.bar(categorias, quantidades)
#plt.show()

#porque que deu uma tabela por aqui? sendo que com o value counts deveria dar valores
#o que eu escrevi ali vai me devolver toda a tabela com benigno para real
#mas eu quero contar somente uma coluna, então tenho que falar que é ela

print(f'a quantidade foi de {teste.values}')

categorias = ['real maligna', 'real benigna'] 
quantidades  = teste.values[0],teste2.values[0]
quantidades_mesmo =  [quantidades[0],quantidades[1]]

plt.figure(1)
plt.bar(categorias, quantidades)
plt.plot()
#plt.show()


#de algum modo deu certo, dps tenho que trabalhar melhor aq, mas já foi uma grande vitória, bem legal

#agora fazendo o gráfico para predict class

condicao_predita_maligna = data["predicted_class"] == "malign"

condicao_predita_benigna = data["predicted_class"] == "benign"

quant1 = condicao_predita_benigna.value_counts().values

categorias2 = ['predito benigno', 'predito maligno']
quantidade2 = [quant1[0], quant1[1]]

plt.figure(2)

plt.bar(categorias2, quantidade2)
plt.plot()



#deu certo novamente - mas tem que melhorar bastante

plt.figure(3)
plt.hist(data['prob_benign'], bins=30 )

plt.figure(4)
plt.hist(data['prob_malign'], bins=30 )



#sucesso, sigo conseguindo fazer rodar, o que é incrivel, não estou pensanso e mais agindo, mas é assim mesmo


#criando agora o gráfico de dispersão
#eixoX prob_benign e o eixoY prob_malign

dispersao_eixoY = data['prob_malign']
dispersao_eixoX = data['prob_benign']

plt.figure(5)
plt.scatter(dispersao_eixoY, dispersao_eixoX)
plt.xlabel("Probabilidade de Benigno")
plt.ylabel("Probabilidade de Maligno")
plt.plot()

plt.show()

#no scatter faltou a pintura para pontos diferentes, mas acho que estou no caminho, depois eu volto aq e remodelo


condicao_falso_positivo = (data['predicted_class'] == "benign") & (data['real_class'] == "malign")

condicao_falso_negativo = (data['predicted_class'] == "malign") & (data['real_class'] == "benign")

dataframe_intermediario = data[condicao_falso_negativo]
dataframe_intermediario2 = data[condicao_falso_positivo]

quantidade_de_falsos_positivos = dataframe_intermediario['predicted_class'].value_counts().values,dataframe_intermediario['predicted_class'].value_counts.values

categorias22 = ['falsos positivos', 'falsos negativos']

plt.bar(categorias22, quantidade_de_falsos_positivos)
plt.plot()
plt.show()