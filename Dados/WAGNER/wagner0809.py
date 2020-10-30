import matplotlib.pyplot as plt
import numpy as np

region1 = [8.46,9.77,4.56,18.75,11.59,7.59,15.99,5.25,7.39,17.26,19.4]
region2 = [10.53,4,6.66,14.69,9.13,13.23,8.12,16.61,10.76,14.71,6.86,23.3]
region3 = [5.73,7.44,12.79,11.06,16.22,13.6,8.74,9.35,9.8,6.26,12,8.95,13.85]

education1 = [4,8.46,6.66,4.56,5.25,9.8,6.26,6.86,12,7.39,8.95,13.85]
education2 = [5.73,7.44,14.69,9.13,11.06,9.77,13.23,8.12,11.59,7.59,13.6,15.99,16.61,10.76,8.74,9.35,14.71,19.4]
education3 = [10.53,12.79,16.22,18.75,23.3,17.26]

plt.figure(figsize=(12,9))

plt.subplot(2,3,1)
plt.tight_layout(pad=2)
plt.title('Distribuição de salários pela região 1')
plt.boxplot(region1)

plt.subplot(2,3,2)
plt.tight_layout(pad=2)
plt.title('Distribuição de salários pela região 2')
plt.boxplot(region2)

plt.subplot(2,3,3)
plt.tight_layout(pad=2)
plt.title('Distribuição de salários pela região 3')
plt.boxplot(region3)

plt.subplot(2,3,4)
plt.tight_layout(pad=2)
plt.title('Distribuição de salários pelo Gr Edu 1')
plt.boxplot(education1)

plt.subplot(2,3,5)
plt.tight_layout(pad=2)
plt.title('Distribuição de salários pelo Gr Edu 2')
plt.boxplot(education2)

plt.subplot(2,3,6)
plt.tight_layout(pad=2)
plt.title('Distribuição de salários pelo Gr Edu 3')
plt.boxplot(education3)

plt.show()
