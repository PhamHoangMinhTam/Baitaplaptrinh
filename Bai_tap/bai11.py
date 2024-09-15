# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:32:02 2024

@author: TAM PC
"""

n = 123456789
m = 0
while n != 0:
    m = (10 * m) + (n % 10)
    n //= 10
    print("m=",m,"n=",n)