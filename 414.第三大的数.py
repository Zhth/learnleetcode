#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        temp = [float("-inf"), float("-inf"), float("-inf")]
        for n in nums:
            if n in temp:
                continue
            if n > temp[0]:
                temp = [n, temp[0], temp[1]]
            elif n > temp[1]:
                temp = [temp[0], n, temp[1]]
            elif n > temp[2]:
                temp[2] = n
        if temp[2] == float("-inf"):
            return temp[0]
        return temp[2]       
# @lc code=end

