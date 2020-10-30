import math

num1 = int(input("Insira seu primeiro número: "))
num2 = int(input("Insira seu segundo número: "))

if (num1 > num2):

    x = num1 - num2

    print("A diferença dos seus números é igual a: " + str(x))

else:

    x = num2 - num1

    print("A diferença dos seus números é igual a: " + str(x))
