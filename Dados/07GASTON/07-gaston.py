import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("axisdata.csv")

plt.figure(figsize=(12, 6))

plt.subplot(2, 3, 1)
plt.tight_layout(pad=2)

plt.subplot(2, 3, 2)
plt.tight_layout(pad=2)

plt.show()

maximo = data.index[data["Cars Sold"] == data["Cars Sold"].max()].tolist()
nomes_max = [
    "August Looner",
    "Brad Withers",
    "Brad Michaels",
    "Brad Baker",
    "Carla Mulgrew",
    "Charles Kennedy",
    "Charles Turner",
    "Charles Davidson",
    "Frank Kane",
    "John Franklin",
    "Lisa Michaels",
    "Onika Turner",
    "Paula Sears",
    "Peter Rogers",
    "Ronelle Turner",
    "Sam Davidson",
    "Sam Turner",
    "Sam Johnson",
    "Sam Monroe",
    "Sam Patterson",
    "Tom Davidson",
    "Tom Kane",
    "Tom Davidson",
    "Victoria Kennedy",
    "Walter Kane",
]

minimo = data.index[data["Cars Sold"] == data["Cars Sold"].min()].tolist()
nomes_min = [
    "Adam Looner",
    "Adam Adams",
    "August Mulgrew",
    "Betty Jackson",
    "Betty Sapp",
    "Betty Kennedy",
    "Brad Vaughn",
    "Brad Mulgrew",
    "Carla Ettienne",
    "Carla Baker",
    "Carla Isaacson",
    "Carla Ettienne",
    "Carla Looner",
    "Carla Jackson",
    "Charles Walters",
    "Charles Walters",
    "Denise Samuelson",
    "Francine Henderson",
    "Frank Johnson",
    "Frank Samuelson",
    "Frank Rogers",
    "Jack Adams",
    "Jack Carter",
    "Jackie Rose",
    "Jackie Franklin",
    "Jada Johnson",
    "Jada Rose",
    "John Mulgrew",
    "Karen Samuelson",
    "Lisa Martins",
    "Mary Franklin",
    "Nicole Moore",
    "Onika Turner",
    "Paula Isaacson",
    "Peter Adams",
    "Peter Davidson",
    "Roger Kennedy",
    "Roger Sapp",
    "Samantha Johnson",
    "Samantha Sears",
    "Samantha Rogers",
    "Tom Looner",
    "Victoria Rogers",
    "Walter Mulgrew",
]

print(f"Média de carros vendidos no ano: {round(data['Cars Sold'].mean())}")

print("------------------------------------------------------------------------")
print(f"O valor máximo de carros vendidos: {data['Cars Sold'].max()}\n")
print(
    f"Os índices dos vendedores são:\n{', '.join(str(i) for i in maximo)}\n\nSeus nomes são:"
)
for i in nomes_max:
    print(i)

print("------------------------------------------------------------------------")
print(f"O valor mínimo de carros vendidos: {data['Cars Sold'].min()}\n")
print(
    f"Os índices dos vendedores são:\n{', '.join(str(i) for i in minimo)}\n\nSeus nomes são:"
)
for i in nomes_min:
    print(i)