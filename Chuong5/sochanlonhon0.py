# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:04:49 2024

@author: TAM PC
"""

n = int(input("Nhập n: "))
S = 0 ;
for i in range(1,n+1):
    if i % 2 == 0: S += i ;
print("Tổng là: ",S)