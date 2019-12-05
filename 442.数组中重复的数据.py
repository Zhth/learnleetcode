#
# @lc app=leetcode.cn id=442 lang=python3
#
# [442] 数组中重复的数据
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # t, res = set(), []
        # for i in nums:
        #     if i in t:
        #         res.append(i)
        #     else:
        #         t.add(i)
        # return res
        if nums:
            l, t, res = len(nums), 0, []
            for i in range(l):
                t = abs(nums[i]) - 1
                if nums[t] > 0:
                    nums[t] = -nums[t]
                else:
                    res.append(t + 1)
            return res 
        return []
        # l, t, res = len(nums), 0, []
        # while t < l:
        #     if nums[t] != t + 1:
        #         if nums[t] == nums[nums[t] - 1]:
        #             t += 1
        #             continue
        #         nums[nums[t] - 1], nums[t] = nums[t], nums[nums[t] - 1]
        #     else:
        #         t += 1
        # for i in range(l):
        #     if i != nums[i] - 1:
        #         res.append(nums[i])
        # return res 
# @lc code=end

