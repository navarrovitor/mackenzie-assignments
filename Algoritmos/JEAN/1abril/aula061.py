#VITOR SANT'ANA NAVARRO 

A = int(input("Qual a medida do lado A? "))

B = int(input("Qual a medida do lado B? "))

C = int(input("Qual a medida do lado C? "))

if A == B == C:
  print("\nSeu triângulo é equilátero.")

elif A != B and A != C and C != B:
  print("\nSeu triângulo é escaleno.")

else:
  print("\nSeu triângulo é isósceles.")


