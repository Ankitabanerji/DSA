"""Date: 23/04/2025"""
from functools import reduce


def hcf(a, b):
    while b:
        a, b = b, a % b
    return a


nums = [48, 180, 240]
result = reduce(hcf, nums)
print("HCF is:", result)
