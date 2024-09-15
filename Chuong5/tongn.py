# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:00:46 2024

@author: TAM PC
"""

so_nguyen = int(input("Nhập một số nguyên dương n: "))
if so_nguyen > 0:
    S = 0
    for i in range(1, so_nguyen + 1):
        S = S + i
    print("Kết quả là: ", S)
else:
    print("Vui lòng nhập số nguyên dương")