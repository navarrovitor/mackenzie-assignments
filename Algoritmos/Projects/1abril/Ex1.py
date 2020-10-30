#VITOR SANT'ANA NAVARRO

opt = str(input("Vamos fazer uma conversão de temperaturas.\nCaso você queira fazer a conversão de Celsius para Fahrenheit, pressione 'c'.\nCaso você queira fazer a conversão de Fahrenheit para Celsius pressione 'f'.\n"))

if opt == 'c':
  tmp = float(input("Qual a temperatura que você deseja converter para Fahrenheit?\n"))
  frht = (1.8 * tmp) + 32
  print("Sua temperatura em Fahrenheit é igual à %f." % frht)

else:
  tmp = float(input("Qual a temperatura que você deseja converter para Celsius?\n"))
  clsus = ((tmp - 32) * 5)/9
  print("Sua temperatura em Celsius é igual à %f." % clsus)