#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        elif num < 0:
            flag = False
        else:
            flag = True
        num = abs(num)
        res = ''
        while num > 0:
            num, t = divmod(num, 7)
            res = str(t) + res
        if flag == False:
            res = '-' + res
        return res

        
# @lc code=end

