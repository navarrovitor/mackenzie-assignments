import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("dados.csv")

label = ['android', 'ios', 'windows', 'others']

periods = data.Period

android = data.Android
ios = data.iOS
windows = data['Windows Phone']
others = data.Others

plt.plot(periods,others,color='blue',marker='d')
plt.plot(periods,windows,color='red',linestyle='dashed',marker='*')
plt.plot(periods,ios,color='olive',linestyle='dashdot',marker='s')
plt.plot(periods,android,color='skyblue',linestyle='dotted',marker='o')

plt.xlabel('Períodos')
plt.title('Série temporal da evolução dos sistemas operacionais')
plt.legend(label)

plt.show()