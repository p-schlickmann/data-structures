"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Input: nums = []
Output: []

Input: nums = [0]
Output: []

Input: nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
Output: [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]

"""


class Solution:
    """
    Two pointers + current index

    1. sort
    2. left pointer = 1 bigger then current index
    3. right pointer = last element
    4. iterate over len of nums - 2
    5. check if element before current index is the same,
    if it is, continue for loop, no need to repeat the last operation
    6. while left < right sum all three pointers, then
    if sum is positive move right pointer, if negative move left pointer, if 0 add pointers to resolution array
    move right and left pointers until the next element is not repeated

    """
    def threeSum(self, nums):
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            left_pointer, right_pointer = i + 1, n - 1
            while left_pointer < right_pointer:
                pointers_sum = nums[i] + nums[left_pointer] + nums[right_pointer]
                if pointers_sum > 0:
                    right_pointer -= 1
                elif pointers_sum < 0:
                    left_pointer += 1
                else:  # pointers_sum == 0
                    res.append([nums[i], nums[left_pointer], nums[right_pointer]])
                    while left_pointer < right_pointer and nums[right_pointer-1] == nums[right_pointer]:
                        right_pointer -= 1
                    while left_pointer < right_pointer and nums[left_pointer+1] == nums[left_pointer]:
                        left_pointer += 1
                    right_pointer -= 1
                    left_pointer += 1
        return res

solution_instance = Solution()
print(solution_instance.threeSum([-1, 0, 1, 2, -1, -4]))
print(solution_instance.threeSum([]))
print(solution_instance.threeSum([0]))
a = solution_instance.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6])
print(a)
print(a == [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]])
