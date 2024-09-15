# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:54:24 2024

@author: TAM PC
"""
n = int(input())
print("Danh sách các ước số của ", n, " là")
for i in range(1, n+1):
    if (n % i == 0):
        print(i, end=",")
