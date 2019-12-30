#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#

# @lc code=start
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                t1, t2 = 10000,10000
                if matrix[i][j] != 0:
                    if i > 0:
                        t1 = matrix[i - 1][j]
                    if j > 0:
                        t2 = matrix[i][j - 1]                   
                    matrix[i][j] = min(t1, t2) + 1
        for i in range(m - 1, -1 ,-1):
            for j in range(n - 1, -1, -1):
                t1, t2 = 10000,10000
                if matrix[i][j] != 0:
                    if i < len(matrix) - 1:
                        t1 = matrix[i + 1][j]
                    if j < len(matrix[0]) - 1:
                        t2 = matrix[i][j + 1]
                    matrix[i][j] = min(matrix[i][j], min(t1, t2) + 1)
        return matrix      
# @lc code=end

