# -*- coding: utf-8 -*-

x = int(raw_input("Введите, пожалуйста, целое число: "))

if x < 0:
    x = 0
    print 'Отрицательное значение изменено на ноль'
elif x == 0:
    print 'Ноль'
elif x == 1:
    print 'Единица'
else:
    print 'Больше'
