"""Date: 5th May 2025
EASY
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true"""

def isValid(s):
    hashmap = {")":"(", "}":"{", "]":"["}
    stack = []
    for i in s:
        if i in hashmap.values():
            stack.append(i)
        elif i in hashmap.keys():

            if stack and hashmap[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    if stack:
        return False
    else:
        return True


print(isValid(']'))
print(isValid('()){'))
print(isValid('()'))
print(isValid('()[]{}'))
print(isValid('(]'))
print(isValid('([)]'))
print(isValid(''))
