# -*- coding: utf-8 -*-


def milk(fn):
    def wrapped():
        return fn() + " + Milk"
    return wrapped
    
def water(fn):
    def wrapped():
        return fn() + " + Water"
    return wrapped


@milk   
@water
def coffee():
    return "Coffee"
   
#newproduct = milk(water(coffee))
#print newproduct()

print coffee()
