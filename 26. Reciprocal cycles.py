# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 14:04:17 2014

@author: raffaelerainone
"""

def find_period(x,d):
#The following conputes the period of x/d when x<d.
    period = 1
    reminders = [0]
    m = (10*x)%d#problem if 10*x < d!!!!
    reminders.append(m)
    if m==0:
        period = 0
    else:
        while m not in reminders:
            m = (10*m)%d
            reminders.append(m)
            if m == 0:
                period = 0
            else:
                period += 1
    if period == 0:
        return period
    else:
        return reminders,m

print find_period(1,6)
'''
result = 7
for d in range(8,1000):
    if result < find_period(1,d):
        result = find_period(1,d)
print result
'''