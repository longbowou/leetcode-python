# 75. Sort Colors
# https://leetcode.com/problems/sort-colors/description
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# 
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# 
# You must solve this problem without using the library's sort function.
# 
#  
# 
# Example 1:
# 
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
# 
# Input: nums = [2,0,1]
# Output: [0,1,2]
#  
# 
# Constraints:
# 
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
#  
# 
# Follow up: Could you come up with a one-pass algorithm using only constant extra space? 


from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0

        def swap(k, l):
            nums[k], nums[l] = nums[l], nums[k]

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1

            i += 1
