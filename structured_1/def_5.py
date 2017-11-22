# -*- coding: utf-8 -*-

#Rab 
#N-22%
#VZ-1.5%
#PS-18%

def vz(amount):
    return amount*0.015
    
def nl(amount):
    return amount*0.22
    
def ps(amount):
    return amount*0.18
    
def zp(amount):
    return amount-vz(amount)-nl(amount)
    
def zp_dirty(amount):
    return amount

def summ_zp(amount):
    return amount+ps(amount)
    
pred = {
    'director': 32000, 
    'engineer': 15000,
    'buch': 3200,
}

ivanov = 100

for im, sm in pred.iteritems():
    print im, zp_dirty(sm), zp(sm), summ_zp(sm )

