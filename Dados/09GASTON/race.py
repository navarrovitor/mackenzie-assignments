import numpy as np
import matplotlib.pyplot as plt

objects = (
    "Brancos",
    "Hispânicos",
    "Pretos",
    "Asiáticos",
    "Multiraciais",
    "Outros",
    "Nativos",
    "Ilhéu",
)
x_pos = np.arange(len(objects))
performance = [55, 25, 17, 3, 2.8, 0.6, 0.3, 0.19]
colors = [
    "darkblue",
    "slateblue",
    "rebeccapurple",
    "darkviolet",
    "violet",
    "fuchsia",
    "deeppink",
    "crimson",
]
plt.bar(x_pos, performance, align="center", color=colors, alpha=1)
plt.xticks(x_pos, objects)
plt.title("Etnias presentes no estado da Flórida!")
plt.show()