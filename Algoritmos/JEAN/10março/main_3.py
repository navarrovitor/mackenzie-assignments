salario = float(input("Qual o seu salário? R$"))
percentual = float(input("Qual o percentual de aumento do seu salário? "))

salarioNovo = (salario * (percentual/100)) + salario

print("Seu salário com o reajuste será igual a R$" + str(salarioNovo))