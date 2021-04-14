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
        totol_len = len(nums1)

        i = totol_len - 1
        p = m - 1
        q = n - 1

        while p >= 0 and q >= 0:
            if nums1[p] >= nums2[q]:
                nums1[i] = nums1[p]
                p -= 1
            else:
                nums1[i] = nums2[q]
                q -= 1

            i -= 1

        while q >= 0:
            nums1[i] = nums2[q]
            q -= 1
            i -= 1

        while p >= 0:
            nums1[i] = nums1[p]
            p -= 1
            i -= 1


# @lc code=end
