#Aula 1 Matplotlib

import matplotlib.pyplot as plt
import numpy as np


array_gerado = np.linspace(1, 10, 10)

#print(array_gerado)

#agora vamos gerar um para o eixo y também
#usei o np.roud para dar um arredondinha no número, gosto de treinar com duas casas decimais para ficar mais visual

array_gerado2 = np.round(np.linspace(1,20,10),2)

print(array_gerado2)

#pronto, já temos dois arrays, logos podemos plotar um gráfico, bora pra cima

#grafico1 = plt.plot(array_gerado,array_gerado2)

#para_mostrar_o_grafico = plt.show()

#agora vamos dar uma customizada no nosso gráfico
#titulozi primeiro 

plt.title("Gráficozão de Cria com números sintéticos")

#para_mostrar_o_grafico = plt.show()

# vamos dar nome para os eixos também

#plt.xlabel('Eixo X', fontsize = 16, color="blue" )
#plt.ylabel('Eixo Y', fontsize = 16, color="red" )


#para_mostrar_o_grafico = plt.show()

#prontinho, temos assim, um gráfico customizado e gerado

eixo_x = array_com_pi = np.linspace(0, 2*np.pi,100)
eixo_y = np.sin(eixo_x)

plt.plot(eixo_x, eixo_y)
plt.show()





