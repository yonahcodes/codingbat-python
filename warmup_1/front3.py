"""
Warmup 1 -> front3
------------------

Given a string, we'll say that the front is the first 3 chars of the string. 
If the string length is less than 3, the front is whatever is there. 
Return a new string which is 3 copies of the front.


front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'

Date: 15 01 2025
"""


def front3(str):
  front = str[:3]
  if len(str) < 3:
      front = str
  return front + front + front


# def front3(str):
#   # Figure the end of the front
#   front_end = 3
#   if len(str) < front_end:
#     front_end = len(str)
#   front = str[:front_end]
#   return front + front + front

# Could omit the if logic, and write simply front = str[:3]
# since the slice is silent about out-of-bounds conditions.