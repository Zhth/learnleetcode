#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]):
        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        else:
            for i in range(2, len(nums)):
                nums[i] += max(nums[:i-1])
            return max(nums)

        # k = len(nums)
        # if k == 0:
        #     return 0
        # f1 = nums[0]
        # if k == 1:
        #     return f1
        # f2 = max(nums[0], nums[1])
        # if k == 2:
        #     return f2
        # for i in range(k - 2):
        #     f2, f1 = max(nums[i + 2] + f1, f2), f2
        # return f2
        
# @lc code=end

