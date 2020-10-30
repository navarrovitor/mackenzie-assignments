import random

def contem(v, qtd, e):
    for i in range(qtd):
        if v[i] == e:
            return i
    return False

def sortear(v):
    qtd = 0
    n = len(v) * 10
    while (qtd < len(v)):
        e = random.randint(1,n)
        if not contem(v,qtd,e):
            v[qtd] = e
            qtd += 1

def sortear_ord(v):
    qtd = 0
    inicial = 1
    final = len(v) * 10
    while(qtd < len(v)):
        e = random.randint(inicial,final)
        v[qtd] = e
        qtd += 1
        inicial = e + 1
        final = e + len(v)*10

def busca_seq(v, elemento):
    cont = 0
    for i in range(0, len(v),1):
        cont += 1
        if v[i] == elemento:
            return(i, cont)
    return(-1, cont)

def busca_binaria(lista, x):
    primeiro = 0
    ultimo = len(lista) - 1
    cont = 0
    while primeiro <= ultimo:
        cont += 1
        meio = (primeiro + ultimo)//2
        if lista[meio] == x:
            return(meio, cont)
        else:
            if x < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    return(-1, cont)

def bubble_sort(v):
    n = len(v)
    cont = 0
    for i in range(n-1):
        for j in range(0,n-i-1):
            if v[j] > v[j+1]:
                cont += 1
                v[j], v[j+1] = v[j+1], v[j]
    return cont