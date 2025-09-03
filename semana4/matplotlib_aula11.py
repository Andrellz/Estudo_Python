'''Aula 11 - Outros tipos de gráfico'''


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as st


import numpy as np
import matplotlib.pyplot as plt

eixo_y = np.arange(0,100)
plt.figure('Seno e Cosseno')
numero_gerado = np.linspace(-np.pi,2*np.pi,100)
numero_gerado2 = np.linspace(-np.pi,2*np.pi,100)

eixo_y_cos = np.cos(numero_gerado)
eixo_y_sin = np.sin(numero_gerado)

eixo_y_cos2 = np.cos(numero_gerado2)
eixo_y_sin2 = np.sin(numero_gerado2)

plt.style.use("ggplot")
plt.figure(1)
plt.plot(numero_gerado, eixo_y_cos)
plt.plot(numero_gerado,eixo_y_sin)
plt.title("Gráfico Seno e Cosseno")
plt.xlabel('Tempo')
plt.ylabel('Amplitude')

plt.show()

#Aparentemente o ggplot é o mais maneiro