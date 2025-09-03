'''Exercício de Pandas'''



import numpy as np
import pandas as pd

caminho_do_csv_para_analise = r"C:\Users\andre\Downloads\classification_results_trial_0001.csv"

arquivo = pd.read_csv(caminho_do_csv_para_analise)

data = pd.DataFrame(arquivo)

#print(data.head())

#Quantas imagens do conjunto são "benigno" e "maligno"?
#para isso valor usar um value_counts para encontrar a quantidade de cada termo na coluna real_class

cond_quant_benignos = data['real_class'] == 'benign'
cond_quant_malignos = data['real_class'] == 'malign'


#print(data[cond_quant_benignos].shape[0])

print(f'A quantidade de begninos é {data[cond_quant_benignos].shape[0]} e a de malignos é {data[cond_quant_malignos].shape[0]}')


#2. Identifique em quais imagens o modelo errou a predição;
#Para isso vamos encontrar as colunas em que a real e a predição são diferentes

print(data.columns)

condicao_falso_predict = data['real_class'] != data['predicted_class']

print(f'As imagens em que foi errado o indice são {data[condicao_falso_predict]['image_path'].to_list()}')

#depois descobrir como que tira esses [] da resposta

#3. Verifique se o modelo estava confiante mesmo quando errou a predição;

#print(data.head())

#para responder a terceira questão, vamos avaliar se os errados tinham muita porcentagem de para o erro ou não


condicao_falso_predict = (data['real_class']) != (data['predicted_class'])
condicao_percentual_benigno = (data['predicted_class'] == "benign") & (data['prob_benign'] > 0.5)
condicao_percentual_maligno = (data['predicted_class'] == "malign") & (data['prob_malign'] > 0.5)

quantidade_de_analises_erradas_malignas = data[condicao_falso_predict & condicao_percentual_maligno].shape[0]
quantidade_de_analises_erradas_benignas = data[condicao_falso_predict & condicao_percentual_benigno].shape[0]


print(f'Portanto podemos concluir que a quantidade de predições erradas com prob acima de 0.5 foi para malignas {quantidade_de_analises_erradas_malignas} e para benignas {quantidade_de_analises_erradas_benignas}')

'''
4. Calcule:
    1. Verdadeiros Positivos (TP) - real maligno, previsto maligno.
    2. Verdadeiros Negativos (TN) - real benigno, previso benigno.
    3. Falsos Positivos (FP) - real benigno, previsto maligno.
    4. Falsos Negativos (FN) - real maligno, previsto benigno.
'''

condicao_tp = (data['real_class'] == 'malign') & (data['predicted_class'] == 'malign')


condicao_tn = (data['real_class'] == 'benign') & (data['predicted_class'] == 'benign')

condicao_fp = (data['real_class'] == 'benign') & (data['predicted_class'] == 'malign')

condicao_fn = (data['real_class'] == 'malign') & (data['predicted_class'] == 'benign')

print(f'Para os casos em questão vamos ter \n TP:{data[condicao_tp].shape[0]} \n TN:{data[condicao_tn].shape[0]} \n FP:{data[condicao_fp].shape[0]} \n FN:{data[condicao_fn].shape[0]}  ')


''' 
5. Calcule:
    1. Acurácia: (TP+TN)/(TP+TN+FP+FN)
    2. Precisão (Precision): TP/(TP+FP) (relevante para os casos preditos como positivos)
    3. Recall: TP/(TP+FN) (relevante para os casos reais positivos)
    4. Especificidade: TN/(TN+FP) (relevante para os casos reais negativos)
'''



tp= data[condicao_tp].shape[0]
tn=  data[condicao_tn].shape[0]
fp= data[condicao_fp].shape[0]
fn=  data[condicao_fn].shape[0]  

acuracia = (tp+tn)/(tp+tn+fp+fn)
precisao = tp/(tp+fp)
recall = tp/(tp+fn)
especificidade = tn/(tn+fp)

print(f'Assim temos para os valores de Acurácia, Precisão, Recall, Especificidade respectivamente: {acuracia:.4f} {precisao:.4f} {recall:.4f} {especificidade:.4f}')

''' 
6.
Encontre as 5 imagens "benigno" com a menor probabilidade de serem "benigno" (prob_benign). O que isso pode indicar?
'''

#Aqui vamos precisar dar uma ordenada nas imagens, vamo pra cima!

condicao6 = data['real_class'] == 'benign'

print(data[condicao6].sort_values(by='prob_benign').head())


''' 7 '''

condicao7 = data['real_class'] == 'malign'

print(data[condicao7].sort_values(by='prob_malign').head())
