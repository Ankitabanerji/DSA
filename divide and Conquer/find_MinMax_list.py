"""Date: 24th April 2025"""

def minMax_dac(arr, i, j):
    if i == j:
        return arr[i], arr[i]

    elif i == j-1:
        if arr[i]<arr[j]:
            return arr[i], arr[j]
        else:
            return arr[j], arr[i]

    else:
        mid = (i + j)//2
        min1,max1 = minMax_dac(arr, i, mid)
        min2,max2 = minMax_dac(arr, mid + 1, j)

        if min1 < min2:
            min_num = min1
        else:
            min_num = min2

        if max1 > max2:
            max_num = max1
        else:
            max_num = max2
        return min_num,max_num


def minMax_non_recursive(arr):
    min_num = arr[0]
    max_num = arr[0]

    for i in range(len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
        elif arr[i] < min_num:
            min_num= arr[i]
    return min_num,max_num


arr = [25,79, 88, 60, 32, 11, 17,88]
print("Using Recursion", minMax_dac(arr,0,len(arr)-1))
print("Using Non-Recursion", minMax_non_recursive(arr))

"""Recursive Approach:
Time Complexity: `O(n)`
- Every element is visited once, and operations per level are constant.
Space Complexity: `O(log n)` (due to recursion stack)
- The depth of the recursion is log(n) for divide-and-conquer.

Iterative (Non-Recursive) Approach:
Time Complexity: `O(n)`
- You look at each of the `n` elements once.
Space Complexity: `O(1)`
- Only a fixed amount of space for `min_val` and `max_val`.

"""
