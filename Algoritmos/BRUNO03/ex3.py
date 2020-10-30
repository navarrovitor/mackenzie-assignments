def busca_seq(v, qtd, elemento):
    for i in range(qtd):
        if v[i] == elemento:
            return i
    else:
        return -1
        
def inserir_ord(v, qtd, elemento):
    is_sorted = False
    for l in range(qtd):
        if v[l] > v[l-1]:
            is_sorted = True
        if is_sorted:
            for i in range(qtd):
                if v[i] > elemento:
                    x = i
                    break
            y = [0]*(qtd+1)
            for j in range(x):
                y[j] = v[j]
            y[x] = elemento
            for k in range(x+1,len(y)):
                y[k] = v[k-1]
            return y
    else:
        return False

size = int(input("Qual a capacidade do vetor a ser criado? "))

vetor = [0] * size
i = 0

while True:
    escolha = int(input("\n(1) Adicionar um novo elemento na próxima posição livre do vetor\n(2) Mostrar os elementos do vetor\n(3) Buscar um elemento no vetor\n(4) Inserir elemento de forma ordenada\n(0) Sair do programa\nEscolha uma opção: "))
    if escolha == 1:
        if i < size:
            print(f"\nVocê escolheu a primeira opção.\n")
            while True:
                x = int(input("Qual o valor do novo elemento? "))
                if x in vetor:
                    print("\nEscolha um elemento que ainda não foi inserido no array.\n")
                    continue
                else:
                    vetor[i] = x
                    break
            i += 1
        else:
            print("\nNão é possível adicionar um novo elemento.")
        continue

    elif escolha == 2:
        print(f"\nVocê escolheu a segunda opção.\n")
        print(f"Esses são os elementos do seu array:\n{' '.join(str(j) for j in vetor)}")
        continue

    elif escolha == 3:
        print(f"\nVocê escolheu a terceira opção.\n")
        y = int(input("Qual o elemento a ser procurado? "))
        print(f"O seu elemento é o {busca_seq(vetor,size,y) + 1}° no array e está na posição de índice {busca_seq(vetor,size,y)}.")
        continue

    elif escolha == 4:
        print(f"\nVocê escolheu a quarta opção.\n")
        z = int(input("Qual o elemento você quer inserir? "))
        vetor = inserir_ord(vetor,size,z)
        print(f"Seu vetor ficou assim: {' '.join(str(j) for j in vetor)}")
        continue
        
    elif escolha == 0:
        print(f"\nVocê escolheu sair do programa. Até a próxima!")
        break

    else:
      print("\nPor favor, escolha entre 1, 2, 3 ou 0")
      continue