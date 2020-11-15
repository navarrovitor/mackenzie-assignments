# Professor, fui fazendo na pressa e não me liguei que precisava usar orientação de arquivos para realizar os objetivos do exercício.
# O programa funciona como deveria, mas funciona como se fosse uma máquina de arcade nova e todos os recordes precisassem ser escritos
# do começo. Ta bonitinho, pode ver ai. Espero que entenda, obrigado pelo semestre!

# Só me liguei depois de horas fazendo do jeito que pensava ser o certo1

import random, time

print("## Exercício 2 ##")
print("\n## Vamos lançar 3 dados...")
pontuações = {}


def jogar():
    nome = input("\n# Entre seu nome: ")
    time.sleep(1)
    soma = 0
    for i in range(3):
        print("Lançando dado... ", end="")
        time.sleep(1)
        valor = random.randint(1, 6)
        print(valor)
        soma += valor
    if len(pontuações) <= 10:
        pontuações[nome] = soma
    else:
        for i in pontuações:
            if soma > pontuações[i]:
                pontuações[nome] = soma
                break
    print(f"\n## {nome}, você obteve {soma} pontos")


run = True

while run:
    choice = int(input("\n(1)Jogar\n(2)Ver as top 10 pontuações\n(3)Sair\n"))
    if choice == 1:
        jogar()
    elif choice == 2:
        print(f"## Top 10 pontuações ##")
        for x in pontuações:
            print(f"{x} : {pontuações[x]}")
    elif choice == 3:
        run = False