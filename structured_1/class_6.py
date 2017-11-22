# -*- coding: utf-8 -*-

#Rab 
#N-22%
#VZ-1.5%
#PS-18%

class Employer:

    amount = 0
    position =""
    
    def __init__(self, position, amount):
        self.position = position
        self.amount = amount

    def vz(self):
        return self.amount*0.015
        
    def get_position(self):
        return self.position
        
    def nl(self):
        return self.amount*0.22
        
    def ps(self):
        return self.amount*0.18
        
    def zp(self):
        return self.amount-self.vz()-self.nl()
        
    def zp_dirty(self):
        return self.amount

    def summ_zp(self):
        return self.amount+self.ps()
        
class Engineer(Employer):
    def zp(self):
        return (self.amount-self.vz()-self.nl())*10
    
class Buch(Employer):
    pass
    
pred = {
    'director': 32000, 
    'engineer': 15000,
    'buch': 3200,
}

ivanov = 100
Empls =[]
for im, sm in pred.iteritems():
    if im=="engineer":
        Empls.append(Engineer(im, sm))
    elif im=="buch":
        Empls.append(Buch(im, sm))    
    else:
        Empls.append(Employer(im, sm))
    
print Empls

for empl in Empls:
    print empl.get_position(), empl.zp_dirty(), empl.zp(), empl.summ_zp()

