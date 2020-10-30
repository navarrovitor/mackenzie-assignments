import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('airbnb_salvador.csv')
# A leitura do arquivo airbnb_salvador em CSV (comma separated values) é feita, nos possibilitando o uso da variável 'data' sempre que
# quisermos usar dados de dentro da planilha.

print(data.price)
# Com data.price podemos utilizar a coluna price da planilha do airbnb. É feita a impressão de todos os valores de preço presentes
# nesta coluna.

print("Valor mínimo:", min(data.price))
# Aqui nós imprimimos o valor mínimo da coluna price

print("Valor máximo:", max(data.price))
# Aqui nós imprimimos o valor máximo da coluna price
