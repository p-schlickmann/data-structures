"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input
2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
"""


class Solution:
    def rotate(self, matrix):
        # matrix_replica = [element.copy() for element in matrix]
        # n = len(matrix)
        # right_pointer = n - 1
        # for i in range(n):
        #     ii = 0
        #     for row in matrix:
        #         row[i] = matrix_replica[right_pointer][ii]
        #         ii += 1
        #     right_pointer -= 1
        # reverse
        l = 0
        r = len(matrix) - 1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
        # transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)


sol = Solution()
sol.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
