import math

num = int(input("Insira seu número: "))

if (num == 0 or num > 0) :

  x = math.sqrt(num)

  print("A raiz quadrada do seu número é igual a: " + str(x))

else:

  x = num**2

  print("O quadrado do seu número é igual a: " + str(x))