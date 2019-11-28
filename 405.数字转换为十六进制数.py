#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        charList = '0123456789abcdef'
        temp = ''
        for i in range(8):
            n = num & 15
            char = charList[n]
            temp = char + temp
            num = num >> 4
        return temp.lstrip('0')
# @lc code=end