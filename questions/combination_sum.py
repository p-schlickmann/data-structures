"""
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Input:
candidates = [2,3,5,8], target = 8

combs = {(8,)}

iterating over element: 2
calls combinator
arr = [2,3,5], target = 6

iterating over element: 2
calls combinator
arr = [2,3,5], target = 4

iterating over element: 2
comb = calls combinator

arr = [2,3,5], target = 2
iterating over element 2:
finds element 2 that equal target
add it to combs = {(2, )}
calls combinator because returned comb is not an empty set

arr = [2,3,5], target = 2-1 = 1
iterates over three elements and discovers that comb is empty set {}
if comb empty set, dont call anymore

iterating over element: 3
3 is bigger then target, skip
iterating over element: 5
5 is bigger then target, skip
return combs = {(2, )}

goes back to arr = [2,3,5], target = 4
gets response that the comb is {(2,)}
this comb = {(2, 2)}
now iterating over element: 3
gets response that the comb is empty set
this comb = {(2, 2)}
now iterating over element: 5
gets response that the comb is empty set

goes back to arr = [2,3,5], target = 6
now iterating over element: 2
gets response that the comb is {(2, 2)}
this comb = {(2, 2, 2)}

now iterating over element: 3
calls combinator
arr = [2,3,5], target = 3
gets the response that the comb is is {(3,)}
this comb = {(2, 2, 2), (3, 3)}

now iterating over element: 5
calls combinator
arr = [2,3,5], target = 1
gets response that the comb is empty set
this comb = {(2, 2, 2), (3, 3)}

goes back to arr = [2,3,5], target = 8
now iterating over 2:
gets the respons that the comb with this element is {(2, 2, 2), (3, 3)}
now this comb = {(2, 2, 2, 2), (2, 3, 3)}

now iterating over 3:
calls combinator arr = [2,3,5], target = 8-3 = 5



Output: [[2,2,2,2],[2,3,3],[3,5],[8]]
"""


class Solution:
    def combinationSum(self, candidates, target):
        self.sol = []
        self.backtrack(candidates, target, [], 0)
        return self.sol

    def backtrack(self, nums, target, current_solution, k):
        if target == 0:
            self.sol.append(current_solution)

        if target < 0 or k >= len(nums):
            return

        for i in range(k, len(nums)):
            self.backtrack(nums, target - nums[i], current_solution + [nums[i]], i)

    # def combinationSum(self, candidates, target, recursive=False):
    #     candidates = set(candidates)
    #     combinations = set()
    #     if target in candidates and not recursive:
    #         combinations.add((target,))
    #         candidates.remove(target)
    #     for cand in candidates:
    #         if cand > target:
    #             continue
    #         combs = self.combinationSum(candidates, target - cand, recursive=True)
    #         sums = {sum(elem) for elem in combs}
    #         if cand == target or target - cand in sums:
    #             if combs:
    #                 for comb in combs:
    #                     combinations.add(tuple(sorted((cand,) + comb)))
    #             else:
    #                 combinations.add((cand,))
    #     return combinations


sol = Solution()
print(sol.combinationSum([2,3,5,8], 8))
