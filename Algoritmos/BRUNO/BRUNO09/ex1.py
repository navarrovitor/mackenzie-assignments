from statistics import mean

linhas = open("filmes_notas.txt").read().splitlines()
filmes = []

print("## Exercício 1 ##\n\n## Lista de filmes:")
y = []
z = []
for i in linhas:
    x = i.split(":")
    y.append(x[0])
    z.append(float(x[1]))

for i in y:
    print(f"- {i}")

print(f"## Média das notas: {round(mean(z),2)}")
