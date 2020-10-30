#VITOR SANT'ANA NAVARRO
import time

turns = None
x = 0

while x == 0:
  turns = int(input("Quantas partidas você quer jogar?\n"))
  if turns > 10:
    print("Escolha um número válido de partidas")
    continue
  else:
    break

count1 = 0
count2 = 0

while count1 < turns or count2 < turns:

  entry1 = str(input("\033[2JOlá jogador número 1, o que você escolhe? Pedra, papel ou tesoura?\n"))

  entry2 = str(input("\033[2JOlá jogador número 2, o que você escolhe? Pedra, papel ou tesoura?\n"))

  jog1 = entry1.upper()
  jog2 = entry2.upper()

  print("O jogador número 1 escolheu %s." % entry1 + "\nO jogador número 2 escolheu %s." % entry2 + "\n")

  if jog1 == "PEDRA" and jog2 == "TESOURA":

    print("O jogador número 1 ganha essa partida!")
    count1 += 1


  elif jog1 == "PAPEL" and jog2 == "PEDRA":

    print("O jogador número 1 ganha essa partida!")
    count1 += 1

  elif jog1 == "TESOURA" and jog2 == "PAPEL":

    print("O jogador número 1 ganha essa partida!")
    count1 += 1

  elif jog2 == "PEDRA" and jog1 == "TESOURA":

    print("O jogador número 2 ganha essa partida!")
    count2 += 1

  elif jog2 == "PAPEL" and jog1 == "PEDRA":

    print("O jogador número 2 ganha essa partida!")
    count2 += 1

  elif jog2 == "TESOURA" and jog1 == "PAPEL":

    print("O jogador número 2 ganha essa partida!")
    count2 += 1

  elif jog1 == jog2:

    print("Foi um empate!")

  else:
    print("Por favor, escolha uma opção válida.")
    time.sleep(5)
    continue
  
  if count1 == turns:
    print("\nO jogador número 1 vence!")
    break
  
  elif count2 == turns:
    print("\nO jogador número 2 vence!")
    break
    
  else:
    print("\n\nPLACAR:\nJogador 1: %i" % count1 + "\nJogador 2: %i\n" % count2)
    time.sleep(5)
    continue

print("Fim de jogo.")
