import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("axisdata.csv")

plt.figure(figsize=(12, 6))

plt.subplot(2, 3, 1)
plt.tight_layout(pad=2)

plt.subplot(2, 3, 2)
plt.tight_layout(pad=2)

plt.subplot(2, 3, 3)
plt.tight_layout(pad=2)

plt.subplot(2, 3, 4)
plt.tight_layout(pad=2)

plt.subplot(2, 3, 5)
plt.tight_layout(pad=2)

plt.subplot(2, 3, 6)
plt.tight_layout(pad=2)

plt.show()