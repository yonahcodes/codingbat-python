"""
Warmup 2 -> front_times
------------------------

Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, 
or whatever is there if the string is less than length 3. Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'

Date: 17 01 2025
"""

def front_times(str, n):
    front = str[:3]
    return front * n


# def front_times(str, n):
#   front_len = 3
#   if front_len > len(str):
#     front_len = len(str)
#   front = str[:front_len]
  
#   result = ""
#   for i in range(n):
#     result = result + front
#   return result