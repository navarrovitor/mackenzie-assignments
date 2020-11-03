import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("axisdata.csv")

years = {}
for i in range(1, 6):
    years[i] = data.query(f"`Years Experience` == {i}")["Cars Sold"].mean()

print(
    f"A média de carros vendidos no ano foi igual a {round(data['Cars Sold'].mean())}"
)

print("------------------------------------------------------------------------")
print(f"O máximo de carros vendidos foi {data['Cars Sold'].max()}\n")
print(f"Os nomes dos vendedores são:")
for i in data.index[data["Cars Sold"] == data["Cars Sold"].max()].tolist():
    print(data.loc[[i]].to_dict()["Fname"][i], data.loc[[i]].to_dict()["Lname"][i])
print("------------------------------------------------------------------------")
print(f"O mínimo de carros vendidos foi {data['Cars Sold'].min()}\n")
print(f"Os nomes dos vendedores são:")
for i in data.index[data["Cars Sold"] == data["Cars Sold"].min()].tolist():
    print(data.loc[[i]].to_dict()["Fname"][i], data.loc[[i]].to_dict()["Lname"][i])

print("------------------------------------------------------------------------")
print(
    f"A média de horas trabalhadas para as pessoas que vendem mais de três carros foi igual a {round(data.query('`Cars Sold` > 3')['Hours Worked'].mean())}"
)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.tight_layout(pad=2)
gen = data["Gender"].value_counts()
colors = ["#23C9FF", "#D90368"]
plt.pie(gen, autopct="%1.2f%%", colors=colors)
plt.title("Taxa de vendas por gênero (F e M)")
plt.legend("M" "F")

plt.subplot(1, 2, 2)
plt.tight_layout(pad=2)
for key in years:
    plt.bar(key, years[key], align="center", width=1, color="#3C6997")
plt.xlabel("Anos de Experiência")
plt.ylabel("Média de horas trabalhadas")
plt.title("Média das horas trabalhadas para cada valor da experiência")

plt.show()