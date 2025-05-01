"""Date: 24th April 2025"""


def binary_search_non_recursion(arr,target):
    i, j = 0, len(arr)-1

    while i <= j:
        mid = (i+j)//2

        if arr[mid] == target:
            return mid

        elif target < arr[mid]:
            j = mid-1
        else:
            i = mid + 1
    return -1


def binary_search_recursion_DAC(arr, target, i, j):
    if i > j:
        return -1  # Target is not in the list

    mid = (i + j) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursion_DAC(arr, target, mid + 1, j)
    else:
        return binary_search_recursion_DAC(arr, target, i, mid - 1)

arr = [1, 3, 5, 7, 9, 11, 13]
print("Using Non-Recursion", binary_search_non_recursion([1,3,5,6],2))
print("Using Recursion DAC", binary_search_recursion_DAC(arr,9,0,len(arr)-1))