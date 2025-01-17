"""
Warmup 2 -> string_times
------------------------

Given a string and a non-negative int n, return a larger string that is n copies of the original string.

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'

Date: 16 01 2025
"""


def string_times(str, n):
    return str * n

print(string_times("Hi", 1))