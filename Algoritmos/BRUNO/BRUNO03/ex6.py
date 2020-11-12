import random

def intercalar_diferentes(v1, v2, vf):
    if len(v1) > len(v2):
        maior, menor = v1, v2
    elif len(v1) < len(v2):
        maior, menor = v2, v1
    else:
        menor = v1
    x = 0
    for i in range(len(menor)):
        vf[x] = v1[i]
        x += 1
        vf[x] = v2[i]
        x += 1
    if len(v1) == len(v2):
        return vf
    else:
        aux1, aux2= len(vf) - (len(maior) - len(menor)), len(maior) - (len(maior) - len(menor))
        for k in range(aux1,len(vf)):
            vf[k] = maior[aux2]
            aux2 += 1
    return vf

def contem(v, qtd, e):
    for i in range(qtd):
        if v[i] == e:
            return True
    return False

def gerar(v1, v2):
    qtd_v1 = 0
    qtd_v2 = 0
    n = (len(v1) + len(v2)) * 5
    while (qtd_v1 < len(v1)):
        e = random.randint(1, n)
        if not contem(v1, qtd_v1, e) and not contem(v2, qtd_v2, e):
            v1[qtd_v1] = e
            qtd_v1 += 1
    while (qtd_v2 < len(v2)):
        e = random.randint(1, n)
        if not contem(v1, qtd_v1, e) and not contem(v2, qtd_v2, e):
            v2[qtd_v2] = e
            qtd_v2 += 1

n1 = int(input('Número de elementos em v1: '))
n2 = int(input('Número de elementos em v2: '))
v1 = [0] * n1
v2 = [0] * n2
vf = [0] * (len(v1) + len(v2))
gerar(v1, v2)
print('v1:', v1)
print('v2:', v2)
intercalar_diferentes(v1,v2,vf)
print('vf:', vf)