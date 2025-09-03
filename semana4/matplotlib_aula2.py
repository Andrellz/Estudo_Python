'''Aula 2 '''

import numpy as np
import matplotlib.pyplot as plt



#tem uma questão de localização, pois somente estando abaixo da figure(1), já vai considerando tudo


#cada figura é referente a um gráfico

eixo_x = np.linspace(0, 2*np.pi,100)
eixo_y = np.sin(eixo_x)

eixo_x_1 = np.linspace(0, 2*np.pi,100)
eixo_y_2 = np.cos(eixo_x)

plt.figure(1, figsize =(5,3))
plt.plot(eixo_x, eixo_y)
plt.title("Gráfico do cossenos")
#plt.show()

plt.figure(2)
plt.title("Gráfico dos senos")
plt.plot(eixo_x_1, eixo_y_2)

plt.show()

#pra mim pelo menos os gráficos não vieram juntos ainda, tive que fechar para vir o outro

#aaaaaaah, para vir os dois juntos, manda só um plt.show() no final, que ai vem os dois, vamos testar agora:

#deu certo vieram os dois juntos, o que foi bem legal



#para o figsize o padrão é  6,4 por 4,8 polegadas -  curiosidade



