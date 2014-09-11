# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 09:53:01 2014

@author: raffaelerainone
"""

def largest_right(matrix):
    prod = 1
    col = len(matrix[0])
    row = len(matrix)
    for i in range(row):
        j = 0
        while j < col-9:
            if int(matrix[i][j:j+2])*int(matrix[i][j+3:j+5])*int(matrix[i][j+6:j+8])*int(matrix[i][j+9:j+11]) > prod:
                prod = int(matrix[i][j:j+2])*int(matrix[i][j+3:j+5])*int(matrix[i][j+6:j+8])*int(matrix[i][j+9:j+11])
            j += 3
    return prod

def largest_down(matrix):
    prod = 1
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row-3):
        j = 0
        while j < col:
            if int(matrix[i][j:j+2])*int(matrix[i+1][j:j+2])*int(matrix[i+2][j:j+2])*int(matrix[i+3][j:j+2]) > prod:
                prod = int(matrix[i][j:j+2])*int(matrix[i+1][j:j+2])*int(matrix[i+2][j:j+2])*int(matrix[i+3][j:j+2])
            j += 3
    return prod

#Diagonal South-West
def largest_diag_sw(matrix):
    prod = 1
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row - 3):
        j = 0
        while j < col-9:
            if int(matrix[i][j:j+2])*int(matrix[i+1][j+3:j+5])*int(matrix[i+2][j+6:j+8])*int(matrix[i+3][j+9:j+11]) > prod:
                prod = int(matrix[i][j:j+2])*int(matrix[i+1][j+3:j+5])*int(matrix[i+2][j+6:j+8])*int(matrix[i+3][j+9:j+11])
            j += 3
    return prod

#Diagonal South-East
def largest_diag_se(matrix):
    prod = 1
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row - 3):
        j = 9
        while j < col:
            if int(matrix[i][j:j+2])*int(matrix[i+1][j-3:j-1])*int(matrix[i+2][j-6:j-4])*int(matrix[i+3][j-9:j-7]) > prod:
                prod = int(matrix[i][j:j+2])*int(matrix[i+1][j-3:j-1])*int(matrix[i+2][j-6:j-4])*int(matrix[i+3][j-9:j-7])
            j += 3
    return prod


my_file = open('11. Largest product in a grid.txt', 'r')
lines  = my_file.readlines()
my_file.close()

A=[]

A.append(largest_right(lines))
A.append(largest_down(lines))
A.append(largest_diag_sw(lines))
A.append(largest_diag_se(lines))

print A, max(A)