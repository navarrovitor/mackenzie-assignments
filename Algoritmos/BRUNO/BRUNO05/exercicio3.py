from lab5 import gerar_aleatorio, gerar_crescente, gerar_decrescente, insertion_sort

while True:
    n = int(input("n de elementos: "))

    v1 = gerar_aleatorio(n)
    v2 = gerar_crescente(n)
    v3 = gerar_decrescente(n)

    c1 = insertion_sort(v1)
    c2 = insertion_sort(v2)
    c3 = insertion_sort(v3)

    print(f"Aqui esta seus elementos: {c1} {c2} {c3}")




