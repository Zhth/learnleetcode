#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        flag1 = nums[0]
        flag2 = nums[0]
        while True:
            flag1 = nums[flag1]
            flag2 = nums[nums[flag2]]
            if flag1 == flag2:
                break
        flag1 = nums[0]
        while flag1 != flag2:
            flag1 = nums[flag1]
            flag2 = nums[flag2]
        return flag1
        
# @lc code=end

