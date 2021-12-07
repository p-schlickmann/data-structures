"""
Given n non-negative integers a1, a2, ..., an , where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container,
such that the container contains the most water.

Input: height = [1,1]
Output: 1

Input: height = [4,3,2,1,4]
Output: 16

Input: height = [1,2,1]
Output: 2

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = left = 0
        right = len(height) - 1
        while right - left > 0:
            gap = right - left
            if height[right] > height[left]:
                area = height[left] * gap
                left += 1
            else:
                area = height[right] * gap
                right -= 1
            if area > max_area:
                max_area = area
        return max_area


print(Solution().maxArea([1, 1]))
print(Solution().maxArea([4, 3, 2, 1, 4]))
print(Solution().maxArea([1, 2, 1]))
print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

