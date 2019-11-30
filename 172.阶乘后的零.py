#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#
# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return self.countM(n, 5)    
        # count2 = self.countM(n, 2)
        # count5 = self.countM(n, 5)
        # return min(count5, count2)
    def countM(self, n, m):
        t = m
        count = 0
        while t <= n:
            count += (n // t)
            t *= m
        return count      
# @lc code=end

