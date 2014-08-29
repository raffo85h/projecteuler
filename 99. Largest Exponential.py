# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 12:52:49 2014

@author: raffaelerainone
"""
from math import log
my_array = []
with open('99. Largest exponential.txt','r') as my_file:
    for line in my_file:
        my_array.append([int(i) for i in line.split(",")])
my_file.close()

max=0
for i in range(1,len(my_array)):
    if my_array[i][1]*(log(my_array[i][0]))>my_array[max][1]*(log(my_array[max][0])):
        max = i
print max+1