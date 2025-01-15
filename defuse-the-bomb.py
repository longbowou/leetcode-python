# https://leetcode.com/problems/defuse-the-bomb/description
# Defuse the Bomb
# You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.
#
# To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.
#
# If k > 0, replace the ith number with the sum of the next k numbers.
# If k < 0, replace the ith number with the sum of the previous k numbers.
# If k == 0, replace the ith number with 0.
# As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].
#
# Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!
#
# 
#
# Example 1:
#
# Input: code = [5,7,1,4], k = 3
# Output: [12,10,16,13]
# Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.
# Example 2:
#
# Input: code = [1,2,3,4], k = 0
# Output: [0,0,0,0]
# Explanation: When k is zero, the numbers are replaced by 0. 
# Example 3:
#
# Input: code = [2,4,9,3], k = -2
# Output: [12,5,6,13]
# Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.
# 
#
# Constraints:
#
# n == code.length
# 1 <= n <= 100
# 1 <= code[i] <= 100
# -(n - 1) <= k <= n - 1
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)

        res = [0] * n
        if k == 0:
            return res

        l = 0
        current_sum = 0
        for r in range(n + abs(k)):
            current_sum += code[r % n]

            if r - l + 1 > abs(k):
                current_sum -= code[l % n]
                l += 1

            if r - l + 1 == abs(k):
                if k < 0:
                    res[(r + 1) % n] = current_sum
                else:
                    res[(l - 1) % n] = current_sum

        return res

        # n = len(code)
        # if k == 0:
        #     return [0 for i in range(n)]

        # code_copy = code.copy()
        # for i in range(n):
        #     s = 0
        #     r1 = []
        #     for j in range(1, abs(k) + 1):
        #         e = i + j if k > 0 else i - j
        #         if k > 0 and e >= n:
        #             e -= n
        #         if k < 0 and e < 0:
        #             e += n
        #         s += code_copy[e]

        #     code[i] = s

        # return code
