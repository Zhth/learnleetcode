#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(2, n+1):
            a, b = b, a+b
        return b
        
# @lc code=end

