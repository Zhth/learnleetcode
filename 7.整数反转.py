#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        flag = -1 if x < 0 else 1
        res = int(str(abs(x))[::-1])
        if -2 ** 31 <= res < 2 ** 31:
            return flag * res
        return 0

        
# @lc code=end

