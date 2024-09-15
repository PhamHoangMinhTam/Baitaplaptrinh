# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:08:29 2024

@author: TAM PC
"""

n=int(input("Nhập số n: "))
s=0
for i in range(0,n):
    s+=1/(i+1)
print("Kết quả:",s)