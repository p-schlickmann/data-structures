"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Input: matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]
Output: [1,2,3,6,9,12,11,10,7,4,5,8]

"""


class Solution:
    def spiralOrder(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])


sol = Solution()
print(sol.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(sol.spiralOrder([[2,5],[8,4],[0,-1]]))
print(sol.spiralOrder([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]))

