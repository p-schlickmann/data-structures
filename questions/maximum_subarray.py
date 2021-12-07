"""
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Contiguous = sharing a common border; touching.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
from math import inf


class Solution:
    def maxSubArray(self, nums):
        """
        Kadane's
        """
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i-1] + nums[i])
        return max(nums)


sol = Solution()
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -1, 4]))
print(sol.maxSubArray([1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4]))
