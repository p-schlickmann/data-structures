"""
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1
"""


class Solution:
    """
    If nums array is empty, return -1

    define two pointers to the borders of the array, 0 and len - 1
    discover which side we are searching
    repeat until we find element
    """

    def search(self, nums, target):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


sol = Solution()
print(sol.search([4, 5, 0, 1, 2, 3, 4], 0))
print(sol.search([4, 5, 6, 7, 0, 1, 2], 3))
print(sol.search([1], 0))
