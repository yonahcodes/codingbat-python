"""
Warmup-1 > pos_neg
------------------

Given 2 int values, return True if one is negative and one is positive.
Except if the parameter "negative" is True, then return True only if both are negative.

pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True

Date: 07 01 2025
"""

def pos_neg(a, b, negative):
    if not negative:
        return (a < 0 and b > 0) or (a > 0 and b < 0)
    else:
        return a < 0 and b < 0


# def pos_neg(a, b, negative):
#   if negative:
#     return (a < 0 and b < 0)
#   else:
#     return ((a < 0 and b > 0) or (a > 0 and b < 0))