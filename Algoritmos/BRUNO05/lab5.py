import random

def contem(v, qtd, e):
    """ verifica se o vetor 'v', que tem 'qtd' elementos, contém o elemento 'e' """
    for i in range(qtd):
        if v[i] == e:
            return True
    return False

def inverter(v):
    """ inverte a ordem dos elementos do vetor 'v' """
    n = len(v)
    for i in range(n//2):
        aux = v[i]
        v[i] = v[n-1-i]
        v[n-1-i] = aux

def gerar_aleatorio(tamanho):
    """ gera um vetor com o tamanho solicitado e elementos pseudo-aleatórios """
    v = [0] * tamanho
    qtd = 0
    n = len(v) * 10
    while (qtd < len(v)):
        e = random.randint(1, n)
        if not contem(v, qtd, e):
            v[qtd] = e
            qtd += 1
    return v

def gerar_crescente(tamanho):
    """ gera um vetor com o tamanho solicitado e elementos pseudo-aleatórios em ordem crescente """
    v = [0] * tamanho
    qtd = 0
    inicial = 1
    final = len(v) * 10
    while (qtd < len(v)):
        e = random.randint(inicial, final)
        v[qtd] = e
        qtd += 1
        inicial = e + 1
        final = e + len(v)*10
    return v

def gerar_decrescente(tamanho):
    """ gera um vetor com o tamanho solicitado e elementos pseudo-aleatórios em ordem decrescente """
    v = gerar_crescente(tamanho)
    inverter(v)
    return v

def bubbleSort(alist):
    """ ordena os elementos do vetor utilizando o algoritmo de ordenação da bolha; 
        retorna o número de execuções do laço de repetição """
    cont = 0
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                cont += 1
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return cont

def selection_sort(v):
    cont = 0
    n = len(v)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if v[j] < v[min]:
                cont += 1
                min = j
        aux = v[i]
        v[i] = v[min]
        v[min] = aux
    return cont

def insertion_sort(v):
    cont = 0
    n = len(v)
    for i in range(1, n):
        aux = v[i]
        aux2 = i - 1
        while aux2 >= 0 and aux < v[aux2]:
            v[aux2 + 1] = v[aux2]
            aux2 -= 1
            cont += 1
        v[aux2 + 1] = aux
    return cont