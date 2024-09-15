# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:10:17 2024

@author: TAM PC
"""

def tim_bo_nghiem(target):
  min_sum = float('inf')
  for x in range(1, target):
    for y in range(1, target - x):
      z = (target - 2*x - 7*y) // 9
      if z > 0 and 2*x + 7*y + 9*z == target and x + y + z < min_sum:
        min_sum = x + y + z
        print(f"Bộ nghiệm: ({x}, {y}, {z})")