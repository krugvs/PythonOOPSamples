# -*- coding: utf-8 -*-

n=input("N")
for x in range(2, n):
    print x
    if n % x == 0:
        print n, 'равно', x, '*', n//x
        break
else:
    # циклу не удалось найти множитель
    print n, '- простое число'

