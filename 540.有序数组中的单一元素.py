#
# @lc app=leetcode.cn id=540 lang=python3
#
# [540] 有序数组中的单一元素
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, l = 0, len(nums)
        while l != 1:
            t = (l+1)//2
            if t%2 == 0:
                if nums[left+t] == nums[left+t-1]:
                    left, l = left, t-1
                else:
                    left, l = left+t, l-t
            else:
                if nums[left+t] == nums[left+t-1]:
                    left, l = left+t+1, l-t-1
                else:
                    left, l = left, t
        return nums[left]

        
# @lc code=end

