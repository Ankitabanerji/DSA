"""
Date: 18th Apr, 2025
Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a
contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices
of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to
the target.
Note: If no such array is possible then, return [-1].

Examples:
Input: arr[] = [1, 2, 3, 7, 5], target = 12
Output: [2, 4]
Explanation: The sum of elements from 2nd to 4th position is 12.

Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 15
Output: [1, 5]
Explanation: The sum of elements from 1st to 5th position is 15.

Input: arr[] = [5, 3, 4], target = 2
Output: [-1]
Explanation: There is no subarray with sum 2."""

class Solution():
    def twoSum(self, arr, target):
        left = 0
        current_sum = 0

        for right in range(len(arr)):
            current_sum += arr[right]

            while (current_sum >target) and (left<=right):
                current_sum -= arr[left]
                left +=1

            if current_sum == target:
                return [left+1, right+1]

        return [-1]


if __name__ == '__main__':
    arr = list(map(int,input("").strip().split()))
    d = int(input().strip())
    ob= Solution()
    result = ob.twoSum(arr,d)
    print(" ".join(map(str,result)))