#
# @lc app=leetcode.cn id=575 lang=python3
#
# [575] 分糖果
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        num = len(candies) // 2
        candielen = len(set(candies))
        return min(num, candielen)
        
            





        
# @lc code=end

