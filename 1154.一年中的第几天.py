#
# @lc app=leetcode.cn id=1154 lang=python3
#
# [1154] 一年中的第几天
#

# @lc code=start
class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = map(int, date.split('-'))
        monthday = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        if m <= 2: return monthday[m - 1] + d
        leap = bool((y%4 == 0 and y%100 != 0) or y%400 == 0) 
        return monthday[m - 1] + d + leap
        
# @lc code=end

