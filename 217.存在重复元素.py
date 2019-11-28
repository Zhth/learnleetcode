#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tempDic = {}
        for num in nums:
            if num in tempDic:
                return True
            tempDic[num] = True
        return False
        
# @lc code=end

