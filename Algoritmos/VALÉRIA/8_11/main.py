from random import randint


def contains(x, y):
    z = []
    for i in range(len(x)):
        for j in x[i]:
            if j in y[i] and j not in z:
                z.append(j)
    insertion_sort(z)
    return z


def insertion_sort(x):
    for i in range(1, len(x)):
        key = x[i]
        j = i - 1
        while j >= 0 and key < x[j]:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = key


def new_array(rows, columns):
    x = []
    for i in range(rows):
        y = []
        for j in range(columns):
            y.append(randint(1, 50))
        x.append(y)
    return x


a = new_array(20, 20)
b = new_array(20, 20)
c = contains(a, b)
print(c)