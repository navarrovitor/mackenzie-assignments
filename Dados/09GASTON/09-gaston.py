import math
import matplotlib.pyplot as plt
import pandas as pd

data_medicare = pd.read_csv("medicare.csv")
data_pneumonia = pd.read_csv("pneumonia.csv")
data_race = pd.read_csv("race.csv")

# plt.figure(figsize=(12, 6))

# plt.subplot(1, 1, 1)
# plt.tight_layout(pad=2)
plt.plot(data_medicare.year, data_medicare.total_reimbursements_b)

# plt.subplot(2, 1, 1)
# plt.tight_layout(pad=2)

# plt.subplot(3, 1, 1)
# plt.tight_layout(pad=2)

plt.show()