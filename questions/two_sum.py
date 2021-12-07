"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


class Solution:
    """
    Add to dictionary what number we need to achieve the target {key: number, value: index of the number}
    then if the current element being iterated is in the dict, it mean we got our target
    """
    def two_sum(self, nums: list, target: int) -> list:
        dic = {}
        for i, value in enumerate(nums):
            if value in dic:
                return [i, dic[value]]
            dic[target - value] = i


sol = Solution().two_sum([2, 15, 11, 7], 9)
print(sol)
