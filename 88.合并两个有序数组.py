#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        while i < m:
            nums.append(nums1[i])
            i += 1
        while j < n:
            nums.append(nums2[j])
            j += 1
        nums1[:] = nums[:]
        return

        
        
# @lc code=end

