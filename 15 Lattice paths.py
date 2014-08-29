# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 16:48:02 2014

@author: raffaelerainone
"""
"""
combinatorially the solution for an nxn grid is (2n choose n),
because we are creating a string with R (right) and D (down): e.g. [rrrddd]
and we want "n" R's and "n" D's. Hence (n+n choose n).
"""
path = 1
for i in range(0,20):
    path=path*(40-i)/(i+1)
print path