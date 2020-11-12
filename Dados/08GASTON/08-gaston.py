import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("08GASTON/gradedata.csv")

length = len(data.index)

sixty = []
seventy = []
eighty = []
ninety = []
for i in data.grade:
    x = i.replace(",", ".")
    if float(x) < 60:
        sixty.append(x)
    elif float(x) == 70:
        seventy.append(x)
    elif float(x) == 80:
        eighty.append(x)
    elif float(x) > 90:
        ninety.append(x)

sixty = len(sixty)
seventy = len(seventy)
eighty = len(eighty)
ninety = len(ninety)

print(
    f"Porcentagem dos alunos com notas:\n\nMenores que 60: {round(((sixty/length)*100),2)}%"
)
print(
    f"Iguais a 70: {round(((seventy/length)*100),2)}%\nIguais a 80: {round(((eighty/length)*100),2)}%"
)
print(f"Maiores que 90: {round(((ninety/length)*100),2)}%")

print("------------------------------------------------------------------------")
corrected_grade = []
for i in data.grade:
    corrected_grade.append(float(i.replace(",", ".")))
print(f"A maior nota foi {max(corrected_grade)}\n")
print(f"Os nomes de quem tirou essa nota são:")
for i in data.index[data.grade == "100"].tolist():
    print(data.loc[[i]].to_dict()["fname"][i], data.loc[[i]].to_dict()["lname"][i])

print("------------------------------------------------------------------------")
print(f"A menor nota foi {min(corrected_grade)}\n")
print(f"Os nomes de quem tirou essa nota são:")
for i in data.index[data.grade == "32"].tolist():
    print(data.loc[[i]].to_dict()["fname"][i], data.loc[[i]].to_dict()["lname"][i])

grades = [sixty, seventy, eighty, ninety]
grades_names = ["<60", "=70", "=80", ">90"]
grades_values = []
for i in grades:
    grades_values.append(round((i / length) * 100, 2))

print("------------------------------------------------------------------------")
print(
    "Visualizando o gráfico de dispersão, é possível notar que quem estudou por mais tempo teve notas melhores."
)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.tight_layout(pad=2)
color_grades = ["#8d99ae", "#2b2d42", "#fcaa67", "#D90368"]
for i in range(len(grades_values)):
    plt.bar(
        grades_names[i],
        grades_values[i],
        align="center",
        width=1,
        color=color_grades[i],
    )
plt.xlabel("Nota")
plt.ylabel("%")
plt.title("Porcentagem de alunos de acordo com as notas")

plt.subplot(1, 2, 2)
plt.tight_layout(pad=2)
plt.scatter(data.hours, corrected_grade, c="g", alpha=0.5)
plt.xlabel("Horas")
plt.ylabel("Nota")
plt.title("Dispersão horas/nota")

plt.show()
