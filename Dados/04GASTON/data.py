import random as rd

zero_to_seventeen = [0] * 9
eighteen_to_forty_four = [18] * 601
forty_five_to_sixty_four = [64] * 3413
sixty_five_to_seventy_four = [74] * 3788
seventy_five_plus = [75] * 7419

a, b, c, d, e = [], [], [], [], []

for i in range(3):
    x = rd.randint(0, 17)
    a.append(x)

for i in range(309):
    x = rd.randint(18, 44)
    b.append(x)

for i in range(1581):
    x = rd.randint(45, 64)
    c.append(x)

for i in range(1683):
    x = rd.randint(65, 74)
    d.append(x)

for i in range(3263):
    x = rd.randint(75, 100)
    e.append(x)

general = a + b + c + d + e