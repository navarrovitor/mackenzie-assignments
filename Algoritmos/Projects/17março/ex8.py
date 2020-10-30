import math

peso = float(input("Qual o peso dos peixes de hoje? "))

if (peso > 50):
  
  exc = peso%50 
  preço = exc * 4.00

  print("Houve excesso de " + str(exc) + "kg e o preço a ser pago é de R$" + str(preço) + ".")

else:
  print("Dentro do regulamento.")
