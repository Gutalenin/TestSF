multipl = 1
summ = 0
for multipl in range(1, 11):
    if multipl % 2 == 0:
        continue
    summ += multipl
    print(summ)