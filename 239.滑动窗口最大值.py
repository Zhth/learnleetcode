#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, res = [], []
        for i in range(len(nums)):
            if not q:
                q.append(i)
            else:
                if i == q[0]+k:
                    q.pop(0)
                while q and nums[q[-1]] < nums[i]:
                    q.pop()
                q.append(i)  
            res.append(nums[q[0]]) 
        return res[k-1:]  
# @lc code=end

