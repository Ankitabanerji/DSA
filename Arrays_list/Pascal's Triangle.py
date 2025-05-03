"""
Date: 2nd May 2025
EASY
Given an integer numRows, return the first numRows of Pascal's triangle.

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]"""
def generate(numRows):
    result = []
    for i in range(numRows):
        if i in [0,1]:
            result.append([1]*(i+1))
        else:
            elem =[]
            for j in range(len(result[-1])):
                if j == 0:
                    elem.append(result[-1][j])
                else:
                    elem.append(result[-1][j] + result[-1][j-1])
            elem.append(1)
            result.append(elem)
    return result

print(generate(0))
print(generate(1))
print(generate(5))
print(generate(6))
