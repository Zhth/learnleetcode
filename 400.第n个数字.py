#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第N个数字
#

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        number = 1
        while n > 0:
            temp = n
            n -= 9*number*10**(number - 1)
            number += 1
        number -= 1
        digit, serial = divmod((temp - 1), number)
        digit += 10**(number - 1)
        digstr = str(digit)
        return(digstr[serial])        
# @lc code=end