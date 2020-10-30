import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("infos_completas.csv")
data_h = pd.read_csv("infos_alturas.csv")
data_w = pd.read_csv("infos_pesos.csv")

plt.figure(figsize=(12, 6))

plt.subplot(2,3,1)
plt.tight_layout(pad=2)
plt.bar(data_h['ALTURA'],data_h['QUANTIDADE'],align='center',width=0.3,color='r')
plt.ylabel('Quantidade de pessoas')
plt.title('Altura dos alunos (Barras)')

plt.subplot(2,3,2)    
plt.tight_layout(pad=2)
plt.pie(data_h['QUANTIDADE'], labels=data_h['ALTURA'],autopct='%1.2f%%')
plt.title('Altura dos alunos (Pizza)')

plt.subplot(2,3,3)    
plt.tight_layout(pad=2)
plt.hist(data_h['QUANTIDADE'],bins=3,color='c')
plt.title('Altura dos alunos (Histograma)')

plt.subplot(2,3,4)
plt.tight_layout(pad=2)
plt.bar(data_w['PESO'],data_w['QUANTIDADE'],align='center',width=0.3,color='y')
plt.ylabel('Quantidade de pessoas')
plt.title('Peso dos alunos (Barras)')

plt.subplot(2,3,5)    
plt.tight_layout(pad=2)
plt.pie(data_w['QUANTIDADE'], labels=data_w['PESO'],autopct='%1.2f%%')
plt.title('Peso dos alunos (Pizza)')

plt.subplot(2,3,6)    
plt.tight_layout(pad=2)
plt.hist(data_w['QUANTIDADE'],bins=3,color='g')
plt.title('Peso dos alunos (Histograma)')

plt.show()