#ENTRADA
AULAS = int(input("Qual o número de aulas que o professor ministra por mês? "))
VALOR = int(input("Qual o valor, em reais, de cada aula que o professor ministra? "))

#PROCESSAMENTO
SALARIO = (AULAS*VALOR)

#SAÍDA
print("O salário desse professor é igual a R$" + str(SALARIO))