import matplotlib.pyplot as plt
num_elementos = [10, 20, 100, 200, 1000, 2000, 10000]
aleatorio = [20, 40, 200, 400, 2000, 4000, 20000]
crescente = [30, 45, 203, 190, 900, 1500, 9000]
decrescente = [1, 4, 10, 40, 1000, 3000, 100000]
plt.plot(num_elementos, aleatorio, 'r')
plt.plot(num_elementos, crescente, 'b')
plt.plot(num_elementos, decrescente, 'g')
plt.xlabel("número de elementos")
plt.ylabel("contador")
plt.show()
