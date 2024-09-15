# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:08:50 2024

@author: TAM PC
"""

n = int(input('Nhập số n : '))
S = 0
for i in range(n + 1) :
 S += (2 * i + 1) / (2 * i + 2)
print('S = ', S)