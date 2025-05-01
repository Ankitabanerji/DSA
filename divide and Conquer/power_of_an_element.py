"""Date: 24th April 2025"""

def power_recursion(a,b):
    """Time Complexity: O(b)
       Space Complexity: O(b)"""
    if b == 1:
        return a
    else:
        return a * power_recursion(a,b-1)


def power_non_recursion(a,b):
    """Time Complexity: O(b)
       Space Complexity: O(1)"""
    res = a
    for i in range(b-1):
        res *= a
    return res


def power_recursive_DAC(a, b):
    """Time Complexity: O(log b)
       Space Complexity: O(log b)"""
    if b == 0:
        return 1
    elif b % 2 == 0:
        half = power_recursive_DAC(a, b // 2)
        return half * half
    else:
        return a * power_recursive_DAC(a, b - 1)


def power_non_recursion_2(a,b):
    """Time Complexity: O(log b)
       Space Complexity: O(1)"""
    result = 1
    while b > 0:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2
    return result


print("Using Recursion linear", power_recursion(3,3))
print("Using Non-Recursion_linear", power_non_recursion(3,3))
print("Using Recursion Divide and Conquer", power_recursive_DAC(3,3))
print("Using Non-Recursion divide", power_non_recursion_2(3,3))