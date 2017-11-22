# -*- coding: utf-8 -*-

x = int(raw_input("Введите, пожалуйста, целое число: "))

while x<=0:
    if x==-20:
        x=0
        continue
    x = int(raw_input("Введите, пожалуйста, целое число: "))
    if x==-10:
        pass
        break
else:
    print "End0"
print "End1"
