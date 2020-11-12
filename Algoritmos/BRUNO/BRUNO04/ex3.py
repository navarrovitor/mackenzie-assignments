from lab4 import sortear, bubble_sort

dados = [0]*10000

for i in range(0,10):
    sortear(dados)
    print(bubble_sort(dados))