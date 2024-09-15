# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:32:25 2024

@author: TAM PC
"""

def fibonacci(n):
  """Tính số Fibonacci thứ n.
  Args:
    n: Vị trí của số Fibonacci cần tính.
  Returns:
    Số Fibonacci thứ n.
  """
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
# In 100 số Fibonacci đầu tiên
for i in range(100):
  print(fibonacci(i))