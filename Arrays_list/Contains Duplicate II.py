"""Date: 3rd May 2025
EASY
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
such that nums[i] == nums[j] and abs(i - j) <= k.
Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false"""
def containsNearbyDuplicate(nums, k):
    hashmap = dict()
    for i in range(len(nums)):
        if (nums[i] in hashmap) and (abs(hashmap[nums[i]] - i) <= k) :
            return True
        else:
            hashmap[nums[i]] = i

    return False

print(containsNearbyDuplicate([1,2,3,1],3))
print(containsNearbyDuplicate([1,0,1,1],1))
print(containsNearbyDuplicate([1,2,3,1,2,3],2))