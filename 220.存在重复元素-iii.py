#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#

# @lc code=start
from collections import OrderedDict
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # https://discuss.leetcode.com/topic/19991/o-n-python-using-buckets-with-explanation-10-lines
        # Bucket sort. Each bucket has size of t. For each number, the possible
        # candidate can only be in the same bucket or the two buckets besides.
        # Keep as many as k buckets to ensure that the difference is at most k.
        buckets = {}
        if t < 0:
            return False
        Set = {}
        for i in range(len(nums)):
            key = nums[i]//(t+1)
            if key in Set:
                Set[key].append(i)
                if Set[key][-1]-Set[key][-2] <= k:
                    return True
            else:
                Set[key] = [i]
            if key+1 in Set and Set[key+1][0]-Set[key][-1] <= k and abs(nums[Set[key+1][0]]-nums[Set[key][-1]]) <= t:
                return True
            if key-1 in Set and Set[key][0]-Set[key-1][-1] <= k and abs(nums[Set[key][0]]-nums[Set[key-1][-1]]) <= t:
                return True
        #print(Set)
                
        return False

        
# @lc code=end

