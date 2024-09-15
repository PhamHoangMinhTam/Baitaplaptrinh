# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:05:27 2024

@author: TAM PC
"""
tong = 0
n = 0
print("Hãy nhập vào số n: ")
n = int(input())
for i in range(1, n + 1):
    tong += 1 / (2 * i + 1)
print("Tổng số là: ", tong)