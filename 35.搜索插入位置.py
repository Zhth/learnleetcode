#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)
        for i in range(l):
            if nums[i] >= target:
                return i
        return l
        
# @lc code=end

