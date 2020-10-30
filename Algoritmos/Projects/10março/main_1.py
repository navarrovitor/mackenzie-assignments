fruta = str(input("Dê o nome de uma fruta: "))
preçoFruta = float(input("Qual o valor dessa fruta? "))
verdura = str(input("Dê o nome de uma verdura: "))
preçoVerdura = float(input("Qual o valor dessa verdura? "))
legume = str(input("Dê o nome de um legume: "))
preçoLegume = float(input("Qual o valor desse legume? "))



print("Aqui estão os nomes de uma fruta, uma verdura e um legume, com seus respectivos preços:\n" + fruta.capitalize() + ": R$" + str(preçoFruta) + ", " + verdura.capitalize() + ": R$" + str(preçoVerdura) + " e " + legume.capitalize() + ": R$" + str(preçoLegume))