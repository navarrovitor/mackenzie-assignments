from exercicio1 import serie1
from exercicio2 import serie2
from exercicio3 import populacao
from exercicio4 import torre_hanoi, pm

print(f"Resultado da série 1 com n = 50: {serie1(50)}\n")
print(f"Resultado da série 1 com n = 100: {serie1(100)}\n")

print(f"Resultado da série 2 com n = 10: {serie2(10)}\n")
print(f"Resultado da série 2 com n = 20: {serie2(20)}\n")

print(f"Número de casais de coelhos com n = 10: {populacao(10)}\n")
print(f"Número de casais de coelhos com n = 20: {populacao(20)}\n")

torre_hanoi(int(input("Quantos anéis serão usados?\n")), 1, 3)