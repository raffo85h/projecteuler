# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 13:31:21 2014

@author: raffaelerainone
"""

import decimal
decimal.getcontext().prec=114

sum = 0
for x in range(0,101):
    if x**0.5%1!=0:
        y = str(x**(decimal.Decimal(0.5)))
        for i in range(0,101):
            if y[i]!=".":
                sum+=int(y[i])
print sum