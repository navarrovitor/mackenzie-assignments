import random

def inserir_ord(v, qtd, e):
  if qtd == 0:
    v[0] = e
    return v
  else:
    for i in range(qtd - 1,-1,-1):
      if v[i] < e:
        print(f'o valor na posição {i} é MENOR que {e}')
        #Da primeira vez que encontrarmos um valor que é menor que o elemento já podemos mover todos os elementos na frente dele uma casa a diante
        try:
          for elem in range(qtd, i + 1, -1): #movendo cada elemento para frente
            v[elem] = v[elem - 1]
          v[i + 1] = e #adicionando "e" na proxima posição do primeiro valor menor que ele
        except Exception as z:
          print(f'O vetor não suporta mais elementos {z}')
        
        return v
      
      elif v[i] > e:
        print(f'o valor na posição {i} é MAIOR que {e}')
      else:
        print(f'o valor na posição {i} é IGUAL a {e}') 
        pass

    for elem in range(qtd, -1, -1): #não foi encontrado nenhum valor menor, portanto ele insere na posição 0
      v[elem] = v[elem - 1]
    v[0] = e
    return v

def intercalar_ord(v1, v2, vf):
    aux1 = 0
    aux2 = 0
    for i in range(len(vf)):
        if aux1 == len(v1):
            vf[i] = v2[aux2]
            aux2 += 1
        elif aux2 == len(v2):
            vf[i] = v1[aux1]
            aux1 += 1            
        elif v1[aux1] <= v2[aux2]:
            vf[i] = v1[aux1]
            aux1 += 1
        else:
            vf[i] = v2[aux2]
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
        # print(f"e: {e}")
        if not contem(v1, qtd_v1, e) and not contem(v2, qtd_v2, e):
            v1 = inserir_ord(v1, qtd_v1, e)
            qtd_v1 += 1
        # print(f"V1: {v1}")
    while (qtd_v2 < len(v2)):
        e = random.randint(1, n)
        # print(f"e: {e}")
        if not contem(v1, qtd_v1, e) and not contem(v2, qtd_v2, e):
            v2 = inserir_ord(v2, qtd_v2, e)
            qtd_v2 += 1
        # print(f"V2: {v2}")
        
n = int(input('Número de elementos em v1 e em v2: '))
v1 = [0] * n
v2 = [0] * n
vf = [0] * (len(v1) + len(v2))
gerar(v1, v2)
print('\nv1:', v1)
print('v2:', v2)
intercalar_ord(v1,v2,vf)
print('vf:', vf)