#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 求众数
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        return max(Counter(nums).items(), key=lambda x:x[1])[0]
        # return Counter(nums).most_common(1)[0][0]
# @lc code=end

