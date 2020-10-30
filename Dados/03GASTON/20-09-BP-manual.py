import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

height = [1.52,1.57,1.57,1.63,1.67,1.68,1.68,1.69,1.7,1.7,1.7,1.73,1.74,1.75,1.75,1.75,1.75,1.78,1.78,1.78,1.78,1.82,1.86,1.87,1.9]
weight = [52,53,55,60,60,62,62,64,68,72,72,72,72,73,74,75,75,75,76,80,83,85,87,94,94]

plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.tight_layout(pad=2)
plt.title('Distribuição de alturas')
plt.boxplot(height)
 
plt.subplot(1,2,2)
plt.tight_layout(pad=2)
plt.title('Distribuição de pesos')
plt.boxplot(weight)

plt.show() 