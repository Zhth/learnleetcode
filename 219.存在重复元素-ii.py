#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        tempDic = {}
        for index, num in enumerate(nums):
            if num in tempDic:
                if index - tempDic[num] <= k:
                    return True
            tempDic[num] = index
        return False
        
# @lc code=end

