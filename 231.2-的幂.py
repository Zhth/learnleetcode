#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        while n != 1:
            n, t = divmod(n, 2)
            if t == 1:
                return False
        return True


        
# @lc code=end

