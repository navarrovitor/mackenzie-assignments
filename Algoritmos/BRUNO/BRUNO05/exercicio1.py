from lab5 import gerar_aleatorio, gerar_crescente, gerar_decrescente, bubbleSort

while True:
    n = int(input("n de elementos: "))

    v1 = gerar_aleatorio(n)
    v2 = gerar_crescente(n)
    v3 = gerar_decrescente(n)

    c1 = bubbleSort(v1)
    c2 = bubbleSort(v2)
    c3 = bubbleSort(v3)

    print(f"Aqui esta seus elementos: {c1}	{c2}	{c3}")




