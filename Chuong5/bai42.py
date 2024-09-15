# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:08:07 2024

@author: TAM PC
"""

n=int(input('n='))
S=0
for i in range (1,n+1):
 S+=i*(i+1)
print('Tổng S là:',S)