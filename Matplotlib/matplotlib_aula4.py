'''Aula 4 de Matplotlib'''

import numpy as np
import matplotlib.pyplot as plt

eixo_y = np.arange(0,100)
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