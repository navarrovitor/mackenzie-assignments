import numpy as np
import matplotlib.pyplot as plt

region = ['Sudeste', 'Nordeste', 'Sul', 'Norte', 'Centro-Oeste']
haddad = np.array([20.8725, 49.82, 19.21, 29.58, 20.59])
ciro = np.array([11.805, 16.21, 8.78, 7.65, 9.7])
bolsonaro = np.array([53.965, 26.87, 58.44, 50.35, 57.67])
ind = np.arange(len(region))

plt.bar(ind, bolsonaro, label='Bolsonaro', color='#D81159', bottom=haddad+ciro)
plt.bar(ind, haddad, label='Haddad' , color='#0496FF' , bottom=ciro)
plt.bar(ind, ciro, label='Ciro', color='#FFBC42')

plt.xticks(ind, region)

plt.ylabel("Votos (%)")
plt.xlabel("Regiões")

plt.legend()
plt.title("Porcentagem de votos das eleições de 2018")
plt.show()