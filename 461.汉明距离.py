#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        hamming = x ^ y
        while hamming & 0xffffffff != 0:
            res += 1
            hamming = hamming & (hamming - 1)
        return res
            
            
            
# @lc code=end
