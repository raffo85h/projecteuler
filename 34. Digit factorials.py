# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 11:38:46 2014

@author: raffaelerainone
"""
from time import time
t = time()

def factorial(n):
    if n>=0:
        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n>1:
            return n*factorial(n-1)
            
def curious_number(n):
    if n<10:
        return False
    else:
        number = str(n)
        sum_number=0
        i=0
        while sum_number<int(n) and i<len(number):
            sum_number+=factorial(int(number[i]))
            i+=1
        if n == sum_number:
            return True

result = 0
for i in range(10,99999):
    if curious_number(i):
        result+=i

print result
print("Time %.2f s" % (time() - t))