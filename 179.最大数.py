#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
class mySmaller(str):
    def __lt__(self, other):
        return self + other > other + self
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = []
        resStr = ''
        for num in nums:
            strs.append(str(num))
        strList = sorted(strs, key=mySmaller)
        res = ''.join(strList)
        if res[0] == '0':
            return '0'
        else:
            return res  

       
# @lc code=end

