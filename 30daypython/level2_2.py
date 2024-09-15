# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:48:35 2024

@author: TAM PC
"""

sum_even = 0  
sum_odd = 0   
for i in range(101): 
    if i % 2 == 0:  
        sum_even += i  
    else:  
        sum_odd += i  
print(f"Tổng của tất cả các số chẵn từ 0 đến 100 là: {sum_even}")
print(f"Tổng của tất cả các số lẻ từ 0 đến 100 là: {sum_odd}")