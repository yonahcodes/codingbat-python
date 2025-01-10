"""
Warmup-1 > front_back
---------------------

Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'

Date: 10 01 2025
"""


def front_back(str):
  if len(str) <= 1:
    return str
  
  first_char = str[0]
  middle = str[1:-1]
  last_char = str[len(str) - 1]
  return last_char + middle + first_char


# def front_back(str):
#   if len(str) <= 1:
#     return str
  
#   mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
#   # last + mid + first
#   return str[len(str)-1] + mid + str[0]