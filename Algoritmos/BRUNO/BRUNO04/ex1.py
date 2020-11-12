from lab4 import contem,busca_seq,sortear

dados = [0]*10
sortear(dados)
sair = False

while not sair:
    print('\n## Menu:\n(1) Mostrar Dados\n(2) Buscar elemento (sequencial)\n(0) Sair')
    opcao = int(input('Escolha uma opção:\n'))
    if opcao == 1:
        print(f'\n## Dados:\n{dados}')
    elif opcao == 2:
        valor = int(input('\n## Elemento a ser buscado:\n'))
        indice, contador = busca_seq(dados,valor)
        print(f'\n## Posição em que o elemento foi encontrado: {indice}\n## Contador de execuções do laço: {contador}')
    elif opcao == 0:
        print("## Você escolheu sair do programa")
        sair = True
    else:
        print("## Opção inválida!")

print("## Fim!")