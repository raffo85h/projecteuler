# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 15:00:17 2014

@author: raffaelerainone
"""

lines = open("12. Large sum.txt","r").readlines()
my_file.close()

sum=0
for i in range(0,100):
    sum+=int(lines[i])
l=len(str(sum))-10
print int(sum/(10**l))