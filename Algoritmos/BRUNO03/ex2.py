def busca_seq(v, qtd, elemento):
    for i in range(qtd):
        if v[i] == elemento:
            return i
    else:
        return -1

qtd = int(input("Qual a capacidade do vetor a ser criado? "))

vetor = [0] * qtd
i = 0

while True:
    escolha = int(input("\n(1) Adicionar um novo elemento na próxima posição livre do vetor\n(2) Mostrar os elementos do vetor\n(3) Buscar um elemento no vetor\n(0) Sair do programa\nEscolha uma opção: "))
    if escolha == 1:
        if i < qtd:
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
        print(f"O seu elemento é o {busca_seq(vetor,qtd,y) + 1}° no array e está na posição de índice {busca_seq(vetor,qtd,y)}.")
        continue
        
    elif escolha == 0:
        print(f"\nVocê escolheu sair do programa. Até a próxima!")
        break

    else:
      print("\nPor favor, escolha entre 1, 2, 3 ou 0")
      continue