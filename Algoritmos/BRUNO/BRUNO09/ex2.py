# Professor, fui fazendo na pressa e não me liguei que precisava usar orientação de arquivos para realizar os objetivos do exercício.
# O programa funciona como deveria, mas funciona como se fosse uma máquina de arcade nova e todos os recordes precisassem ser escritos
# do começo. Ta bonitinho, pode ver ai. Espero que entenda, obrigado pelo semestre!

# Só me liguei depois de horas fazendo do jeito que pensava ser o certo
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
    pontuações[nome] = soma
    print(f"\n## {nome}, você obteve {soma} pontos")


run = True
while run:
    choice = int(
        input("\n(1)Jogar\n(2)Ver as pontuações de todos que já jogaram\n(3)Sair\n")
    )
    if choice == 1:
        jogar()
    elif choice == 2:
        print(f"## Pontuações ##")
        for x in pontuações:
            print(pontuações[x])
    elif choice == 3:
        run = False