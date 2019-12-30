#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # res = []
        # if nums:
        #     n = len(nums)
        #     for i in range(n):
        #         val = abs(nums[i]) - 1
        #         if nums[val] > 0:
        #             nums[val] = -nums[val]
        #     for i in range(n):
        #         if nums[i] > 0:
        #             res.append(i + 1)
        # return res
        if nums:
            l, t, res = len(nums), 0, []
            while t < l:
                if nums[t] != t + 1:
                    if nums[t] == nums[nums[t] - 1]:
                        t += 1
                        continue
                    nums[nums[t] - 1], nums[t] = nums[t], nums[nums[t] - 1]
                else:
                    t += 1
            for i in range(l):
                if i != nums[i] - 1:
                    res.append(i + 1)
            return res
        return []
            


        
# @lc code=end

