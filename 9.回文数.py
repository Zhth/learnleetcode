#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        #     return False
        s = str(x)
        l = len(s)
        for i in range(l // 2):
            if s[i] != s[-i - 1]:
                return False
        return True

        
# @lc code=end

