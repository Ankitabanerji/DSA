"""Date: 5th May 2025
EASY
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 """
def longestCommonPrefix(strs) -> str:
    ans = ""
    strs.sort()
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
        if (first[i] != last[i]):
            return ans
        ans += first[i]
    return ans

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))