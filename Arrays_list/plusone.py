"""Date: 1st May 2025
EASY
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the
integer.
The digits are ordered from most significant to the least significant in left-to-right order. The large integer does not
 contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2]."""


def plusOne(digits):
    i= len(digits)-1
    while i >= 0:
        if digits[i]+1 != 10:
            digits[i] +=1
            return digits

        digits[i] =0

        if i == 0:
            return [1] + digits
        i -=1



print(plusOne([9,9]))
print(plusOne([1,2,3]))
print(plusOne([9]))