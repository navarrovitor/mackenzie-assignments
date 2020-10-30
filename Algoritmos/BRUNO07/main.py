from exercicio1 import serie1
from exercicio2 import inverter
from exercicio3 import contador

print(f"serie1(30) = {serie1(30)}")
print(f"serie1(100) = {serie1(100)}")

word = input("Palavra a ser invertida: ")
array = list(word)
resposta = ''.join(array)
print(inverter(array))

print(contador(int(input("Qual seu N? ")), int(input("Qual seu K? "))))