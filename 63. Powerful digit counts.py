# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 16:58:05 2014

@author: raffaelerainone
"""

'''
---------------------------------------------------------------------
QUESTION:
The 5-digit number, 16807=75, is also a fifth power.
Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
---------------------------------------------------------------------
We want 10^{b-1} < a^b < 10^b
Therefore (Log = log in base 10)
1 - 1/b < Log a < 1
Thus a < 10 (*)

Then we also have
1 - 1/b < Log a ==> b < 1/(1 - Log a) ≤ 1/(1 - Log 9)< 22 (**)

It is clear that n=1 is one of the required integer,
since a^1 = a for all a; in particular for 0 < a < 10. (***)
'''

result = 9 # by (***), so the exponent must be 'b > 1'
for a in range(1,10): # by (*)
    for b in range(2,22): # by (**)
        if len(str(a**b)) == b:
            result +=1
print result