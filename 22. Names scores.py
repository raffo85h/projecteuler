# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 10:34:31 2014

@author: raffaelerainone
"""
names = open("22. Names scores.txt", "r")
names = names.read()
names = names.split(',') #if here I write '","' then "Mary is going to be the 1st!
names = sorted(names)
#print names
def value_letters(letter):
    letter = str(letter)
    alphabet = list(string.ascii_uppercase)
    value = 0
    for i in range(0,len(alphabet)):
        if letter == alphabet[i]:
            value = (i+1)
    return value
    
score=0
for i in range(0,len(names)):
    sum=0
    for j in range(0,len(names[i])):
        sum += int( value_letters(names[i][j]) )
    score+=sum*(i+1)
print score