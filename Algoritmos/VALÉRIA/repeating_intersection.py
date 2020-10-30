def intercarlar_iguais(v1,v2):
    tamanho = 0
    for i in v1:
        if i in v2:
            tamanho += 1

    vf = [0]*tamanho

    index = 0
    for i in v1:
        if i in v2:
            vf[index] = i
            index += 1
    
    for i in range(tamanho-1):
        for j in range(0,tamanho-i-1):
            if vf[j] > vf[j+1]:
                vf[j], vf[j+1] = vf[j+1], vf[j]

    return vf

vetA = [3, 6, 2, 8, 10, 1]
vetB = [4, 2, 5, 1, 9]

print(intercarlar_iguais(vetA,vetB))
