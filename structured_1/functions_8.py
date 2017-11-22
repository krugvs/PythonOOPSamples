# -*- coding: utf-8 -*-

def connect2db1(host, database, login, password):
    print "Connect to DB run. {0}, {1}, {2}, {3}".format(host, database, login, password)
    pass
    
def connect2db2(*args, **kwargs):
    pass
    
def avg(*args):
    avg_s = 0.0
    avg_c = 0.0
    for i in args:
        avg_s = avg_s + i
        avg_c = avg_c + 1
    if avg_c > 0:
        return avg_s/avg_c
    pass
    
def f2(*args, **kwargs):
    print kwargs
    pass
    
host = "localhost"
login = "user"
password = "secretpass"
database = "database_sample_1"

connect2db1(host, database, login, password)
connect2db1(database=database, login=login, password=password, host=host)

print avg(2,4,6,8,10,14,15)
print f2(1,2,4,5,6,8,10,12,stepen=7,chislo=2)
