import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("infos_completas.csv")

plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.tight_layout(pad=2)
plt.title('Distribuição de alturas')
plt.boxplot(data.ALTURA)
 
plt.subplot(1,2,2)
plt.tight_layout(pad=2)
plt.title('Distribuição de pesos')
plt.boxplot(data.PESO)

plt.show() 