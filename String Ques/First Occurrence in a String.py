"""Date:7th May 2025
EASY
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1
if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1."""


def strStr(haystack, needle):
    if len(haystack) < len(needle):
        return -1

    for i in range(len(haystack)):
        if haystack[i:i + len(needle)] == needle:
            return i

    return -1



print(strStr("sadbutsad","sad"))
print(strStr("sabbutsad","sad"))
print(strStr("leetcode","leeto"))