"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

[[4,7],[4,5]]
[[4,7]]

[[5,7],[4,5]]
[[4,7]]
"""


class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


sol = Solution()
print(sol.merge([[1, 3], [2, 6], [3, 7], [8, 10], [15, 18]]))
print(sol.merge([[1, 4], [4, 5]]))
print(sol.merge([[4, 7], [4, 5]]))
print(sol.merge([[5, 7], [4, 5]]))
print(sol.merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
