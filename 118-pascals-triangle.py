# https://leetcode.com/problems/pascals-triangle/description
# 118. Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
#
# 
#
# Example 1:
#
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
#
# Input: numRows = 1
# Output: [[1]]
# 
#
# Constraints:
#
# 1 <= numRows <= 30

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        r = [[1]]

        if numRows == 1:
            return r

        r.append([1, 1])
        i = 2
        while i < numRows:
            c = [1]
            for j in range(len(r[-1]) - 1):
                c.append(r[-1][j] + r[-1][j + 1])
            c.append(1)
            r.append(c)
            i += 1

        return r
