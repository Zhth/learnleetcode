#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(rowIndex//2 + 1):
            t = 1
            for j in range(i):
                t *= rowIndex - j
                t /= j + 1
            res.append(int(t))
        for i in range(rowIndex - rowIndex//2 - 1, -1, -1):
            res.append(res[i])
        return res

# @lc code=end

