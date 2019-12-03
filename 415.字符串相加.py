#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        length1, length2 = len(num1), len(num2)
        addFlag = 0
        while length1 > 0 or length2 > 0:
            temp1 = int(num1[length1 - 1]) if length1 > 0 else 0
            temp2 = int(num2[length2 - 1]) if length2 > 0 else 0
            addFlag, tempRes = divmod(temp1 + temp2 + addFlag, 10)
            res = str(tempRes) + res
            length1 -= 1
            length2 -= 1
        res = '1' + res if addFlag == 1 else res
        return res
        # num1 = int(num1)
        # num2 = int(num2)
        # return str(num1 + num2)       
# @lc code=end

