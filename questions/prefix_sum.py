"""
Given an array of integers, how to perform a prefix sum of all elements?
"""


class Solution:
    def prefix_sum(self, lst):
        prefix_sum = [0 for _ in range(len(lst))]
        prefix_sum[0] = lst[0]
        for i in range(1, len(lst)):
            prefix_sum[i] = prefix_sum[i - 1] + lst[i]
        return prefix_sum


print(Solution().prefix_sum([2, 11, 7, 9]))
