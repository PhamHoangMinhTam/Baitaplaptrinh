# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:09:57 2024

@author: TAM PC
"""

def tim_bo_nghiem_lon_nhat(target):
  max_sum = 0
  for x in range(target//2, 0, -1):
    for y in range((target - 2*x)//7, 0, -1):
      z = (target - 2*x - 7*y) // 9
      if z > 0 and 2*x + 7*y + 9*z == target:
        current_sum = x + y + z
        if current_sum > max_sum:
          max_sum = current_sum
          print(f"Bộ nghiệm: ({x}, {y}, {z})")