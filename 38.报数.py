#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        f = '1'
        for i in range(n - 1):
            res = ''
            t = f[0]
            tn = 0
            for c in f:
                if c == t:
                    tn += 1
                else:
                    res += str(tn) + str(t)
                    t = c
                    tn = 1
            res += str(tn) + str(t)
            f = res
        return f


        
# @lc code=end

