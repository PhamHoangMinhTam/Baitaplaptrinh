# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:30:51 2024

@author: TAM PC
"""

import math
def print_table(values):
  """In bảng giá trị theo định dạng.
  Args:
    values: Danh sách các giá trị cần in.
  """
  for row in values:
    print("\t".join(map(str, row)))
if __name__ == "__main__":
  n_values = [2, 4, 8, 16, 32, 64, 128]
  table_data = []
  for n in n_values:
    log_n = math.log2(n)
    n_log_n = n * log_n
    n_squared = n**2
    n_cubed = n**3
    table_data.append([log_n, n, n_log_n, n_squared, n_cubed])
  print("log(n)\tn\tn*log(n)\tn^2\tn^3")
  print_table(table_data)