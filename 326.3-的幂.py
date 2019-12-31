#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        while n != 1:
            n, t = divmod(n, 3)
            if t != 0:
                return False
        return True

        
# @lc code=end

