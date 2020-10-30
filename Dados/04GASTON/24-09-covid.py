import data
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Baseando-se na planilha covid_data (com todos os dados da Covid-19), 14_04 e 13_05 (que têm as informações de mortes 
# relacionadas ao covid-19 na data 14 de abril e 13 de maio em Nova Iorque), foi possível ser feita a simulação presente em data.py,
# que basicamente gerou as idades de cada morte pela doença. Com isso, foi feito um histograma e uma curva densidade.

data = sorted(data.general)

average = round(np.average(data),3)
variance = round(np.var(data),3)
standard_deviation = round(np.std(data),3)
maximum = max(data)
minimum = min(data)

sentence = f"Média = {average}\nVariância = {variance}\nDesvio Padrão = {standard_deviation}\nValor Máximo = {maximum}\nValor Mínimo = {minimum}"

plt.yticks(np.arange(minimum, maximum, 25))
plt.plot(data,norm.pdf(data, np.mean(data), np.std(data)))
plt.hist(data, density=True, bins=15, color='purple')
plt.text(10,0.02,sentence)
plt.title('Fatalidades da Covid-19 por idade')
# plt.grid(axis='y', linestyle='dotted')
plt.ylabel('Frequência de fatalidades')
plt.xlabel('Idade')

plt.show()