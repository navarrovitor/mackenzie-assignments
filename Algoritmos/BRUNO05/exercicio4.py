import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

num_elementos = [10, 20, 100, 200, 1000, 2000, 10000]

aleatorio_bubble = [16, 95, 2085, 10266, 251838, 1003463, 25076172]
crescente_bubble = [0, 0, 0, 0, 0, 0, 0]
decrescente_bubble = [45, 190, 4950, 19900, 499500, 1999000, 49995000]

aleatorio_selection = [12, 30, 332, 770, 5398, 12724, 77480]
crescente_selection = [0, 0, 0, 0, 0, 0, 0]
decrescente_selection = [25, 100, 2500, 10000, 250000, 1000000, 25000000]

aleatorio_insertion = [20, 122, 2376, 10176, 246733, 975473, 25176299]
crescente_insertion = [0, 0, 0, 0, 0, 0, 0]
decrescente_insertion = [45, 190, 4950, 19900, 499500, 1999000, 49995000]

plt.figure(figsize=(12,6))

plt.subplot(1,3,1)
plt.tight_layout(pad=2)
plt.title('Bubble Sort')
plt.xlabel("número de elementos")
plt.ylabel("contador")
label = ['Aleatório', 'Crescente', 'Decrescente']

plt.plot(num_elementos, aleatorio_bubble, color='blue', linestyle= 'dashed')
plt.plot(num_elementos, crescente_bubble, color='blue', linestyle= 'dotted')
plt.plot(num_elementos, decrescente_bubble, color='blue', linestyle= 'dashdot')

plt.legend(label)

plt.subplot(1,3,2)
plt.tight_layout(pad=2)
plt.title('Selection Sort')
plt.xlabel("número de elementos")
plt.ylabel("contador")
label = ['Aleatório', 'Crescente', 'Decrescente']

plt.plot(num_elementos, aleatorio_selection, color='purple', linestyle= 'dashed')
plt.plot(num_elementos, crescente_selection, color='purple', linestyle= 'dotted')
plt.plot(num_elementos, decrescente_selection, color='purple', linestyle= 'dashdot')

plt.legend(label)

plt.subplot(1,3,3)
plt.tight_layout(pad=2)
plt.title('Insertion Sort')
plt.xlabel("número de elementos")
plt.ylabel("contador")
label = ['Aleatório', 'Crescente', 'Decrescente']

plt.plot(num_elementos, aleatorio_insertion, color='olive', linestyle= 'dashed')
plt.plot(num_elementos, crescente_insertion, color='olive', linestyle= 'dotted')
plt.plot(num_elementos, decrescente_insertion, color='olive', linestyle= 'dashdot')

plt.legend(label)

plt.show()
