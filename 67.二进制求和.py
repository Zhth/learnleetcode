#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        t1 = int(a, 2)
        t2 = int(b, 2)
        return bin(t1 + t2)[2:]



        
# @lc code=end

