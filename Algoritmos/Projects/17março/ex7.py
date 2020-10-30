import math

aval1 = float(input("Insira sua primeira nota: "))
aval2 = float(input("Insira sua segunda nota: "))
aval3 = float(input("Insira sua terceira nota: "))

media = ((aval1 * 2) + (aval2 * 3) + (aval3 * 5))/10

if media >= 6:
  
  print("Parabéns, você foi aprovado!")

else:
  
  print("Boa sorte no próximo semestre, você foi reprovado.")