import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("algebradata.csv")

plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.tight_layout(pad=2)
c_sum = df["Grade"].value_counts()
colors = ["#FFC857", "#E9724C", "#C5283D", "#06D6A0", "#255F85"]
plt.pie(c_sum, autopct="%1.2f%%", colors=colors)
plt.title("Porcentagem das Notas do Alunos por conceito")
plt.legend("A" "D" "B" "C" "F")

plt.subplot(1, 3, 2)
plt.tight_layout(pad=2)
fem = df.query('Grade == "A" & Gender == "F"').count()
masc = df.query('Grade == "A" & Gender == "M"').count()
plt.bar("F", fem, align="center", width=0.3, color="#F08700")
plt.bar("M", masc, align="center", width=0.3, color="#00A6A6")
plt.title("Quantidade de homens e mulheres com conceito A")

plt.subplot(1, 3, 3)
plt.tight_layout(pad=2)
plt.hist(df["Hours of Study"], bins=18, color="#FB62F6")
plt.xlabel("Horas de Estudo")
plt.ylabel("Quantidade de Estudantes")
plt.title("Frequência de Estudos do Alunos")

plt.show()
