#VITOR SANT'ANA NAVARRO
x = float(input("Qual a coordenada X?\n"))
y = float(input("Qual a coordenada Y?\n"))
          
if x == 0 and y == 0:
    print("Seu ponto está na origem.")
elif x == 0 and y != 0:
    print("Seu ponto está no eixo X.")
elif x != 0 and y == 0:
    print("Seu ponto está no eixo Y.")
elif x > 0 and y > 0:
    print("Seu ponto está no Primeiro quadrante.")
elif x < 0 and y > 0:
    print("Seu ponto está no Segundo quadrante.")
elif x < 0 and y < 0:
    print("Seu ponto está no Terceiro quadrante.")
else:
    print("Seu ponto está no Quarto quadrante.")
