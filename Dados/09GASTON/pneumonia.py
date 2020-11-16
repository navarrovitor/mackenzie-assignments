import numpy as np
import matplotlib.pyplot as plt

infarto = [9441, 9314, 8860, 9010, 8657]
pneumonia = [13678, 14358, 13890, 14658, 13355]
insuficiencia = [17275, 16529, 15059, 15117, 14753]
bar_width = 0.25

r1 = np.arange(len(infarto))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

plt.bar(r1, infarto, width=bar_width, color="red", label="infarto")

plt.bar(r2, pneumonia, width=bar_width, color="green", label="pneumonia")

plt.bar(r3, insuficiencia, width=bar_width, color="blue", label="insuficiencia")

plt.ylabel("Total de pacientes")
plt.title("Porcentagem de doenças por ano")
plt.xticks(
    [r + bar_width for r in range(len(infarto))],
    ("2010", "2011", "2012", "2013", "2014"),
)
plt.legend()
plt.show()