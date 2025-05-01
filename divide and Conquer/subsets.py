"""Date: 28th April 2025"""


def print_all_subsets_recursion(arr,ans,i):
    if i == len(arr):
        result.append(ans.copy())
        return
    else:
        ans.append(arr[i])
        print_all_subsets_recursion(arr, ans, i + 1)
        ans.pop()
        print_all_subsets_recursion(arr, ans, i + 1)


result = []
print_all_subsets_recursion([1,2,3],[],0)
print(result)

"""The reason we use current.copy() (or list(current)) is to prevent future modifications from affecting the subsets we've already stored.
Here's the issue:
- In Python, lists are mutable and passed by reference.
- If you just append(current) into result, you're appending a reference to the same current list — not a snapshot of it at that time.
- So later, when you modify current (e.g., by .pop()), it would also modify the subset already saved inside result, which is not what you want.
By doing current.copy(), you make a new independent list at that moment."""