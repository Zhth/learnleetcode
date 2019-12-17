#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        t = 1
        for i in range(len(digits) - 1, -1, -1):
            t, digits[i] = divmod(t + digits[i], 10)
            if t == 0:
                return digits
        digits = [t] + digits
        return digits

        
# @lc code=end

