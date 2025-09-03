'''Aula 3'''


import numpy as np
import matplotlib.pyplot as plt 


#aqui vai ser usada a função arrange. A diferença dela para a linspace é que por meio dela definimos o passo. No caso da outro definimos o ponto final


numero_gerado = np.arange(0,100)
eixo_y_exponencial = np.exp(numero_gerado)

#plt.figure("Exponencial")
#plt.plot(numero_gerado,eixo_y_exponencial)
#plt.show()

print(numero_gerado)


#agora vamos fazer dois intervalos com seno e cosseno para gerar os gráficos juntos


plt.figure('Seno e Cosseno')
numero_gerado = np.linspace(-np.pi,2*np.pi,100)
eixo_y_cos = np.cos(numero_gerado)
eixo_y_sin = np.sin(numero_gerado)     
plt.plot(numero_gerado, eixo_y_cos)
plt.plot(numero_gerado,eixo_y_sin)
plt.title("Gráfico Seno e Cosseno")
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

#deu certo! Assiml, gerou mesmo um gráfico só com as duas representações, bom para gerar comparativos

#print(numero_gerado)

#bem maneiro e o gráfico fica top

