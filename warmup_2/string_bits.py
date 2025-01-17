"""
Warmup 2 -> string_bits
-----------------------

Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'

Date: 19 01 2025
"""


def string_bits(str):
    new_str = ""
    for i in range(len(str)):
        if i % 2 == 0:
            new_str += str[i]
    return new_str


# def string_bits(str):
#   result = ""
#   # Many ways to do this. This uses the standard loop of i on every char,
#   # and inside the loop skips the odd index values.
#   for i in range(len(str)):
#     if i % 2 == 0:
#       result = result + str[i]
#   return result