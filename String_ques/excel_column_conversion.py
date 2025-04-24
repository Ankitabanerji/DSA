"""
Date: 23/04/2025
You are given a string STR representing the column title in an Excel Sheet.
You need to find its corresponding column number.

For example: A corresponds to 1, B to 2, C to 3, … , Z to 26, AA to 27, .. and so on.

input:
3
A
AB
F

output:
1
28
6

input:
3
S
COD
ZZZ

output:
19
2422
18278
"""


def titleToNumber(stringStr):
    count_sum = 0
    for i in range(len(stringStr)):
        count_sum = count_sum * 26 + (ord(stringStr[i]) - ord('A') + 1)
        # count_sum = (count_sum * 26) + ((ord(stringStr[i].upper()) % 65) + 1)

    return count_sum


print(titleToNumber("S"))
print(titleToNumber("COD"))
print(titleToNumber("ZZZ"))