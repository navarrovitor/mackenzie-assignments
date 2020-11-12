#ENTRADA
TEMPO = int(input("Qual foi o tempo gasto na viagem? "))
VELOCIDADE = int(input("Qual foi a velocidade média da viagem? "))

#PROCESSAMENTO
DISTANCIA = (TEMPO*VELOCIDADE)
LITROS_USADOS = DISTANCIA/12

#SAÍDA
print("Com a velocidade média de " + str(VELOCIDADE) + "Km/H durante " + str(TEMPO) + " horas por " + str(DISTANCIA) + " quilômetros, a quantidade de combustível utilizada em tal viagem foi de " + str(LITROS_USADOS) + " litros")