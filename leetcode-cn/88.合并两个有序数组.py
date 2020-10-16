#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        p = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
                p -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
                p -= 1

        while i >= 0:
            nums1[p] = nums1[i]
            i -= 1
            p -= 1
        while j >= 0:
            nums1[p] = nums2[j]
            j -= 1
            p -= 1


# @lc code=end
