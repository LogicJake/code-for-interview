#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        def help(nums1, start1, end1, nums2, start2, end2, k):
            len1 = end1 - start1 + 1
            len2 = end2 - start2 + 1

            # 保证 nums1 较短
            if len1 > len2:
                return help(nums2, start2, end2, nums1, start1, end1, k)

            if len1 == 0:
                return nums2[start2 + k - 1]

            if k == 1:
                return min(nums1[start1], nums2[start2])

            i = start1 + min(k // 2, len1) - 1
            j = start2 + min(k // 2, len2) - 1

            if nums1[i] <= nums2[j]:
                return help(nums1, i + 1, end1, nums2, start2, end2,
                            k - (i - start1 + 1))
            else:
                return help(nums1, start1, end1, nums2, j + 1, end2,
                            k - (j - start2 + 1))

        m = len(nums1)
        n = len(nums2)

        if (m + n) % 2 == 1:
            return help(nums1, 0, m - 1, nums2, 0, n - 1, (m + n + 1) // 2)
        else:
            return (help(nums1, 0, m - 1, nums2, 0, n - 1,
                         (m + n) // 2) + help(nums1, 0, m - 1, nums2, 0, n - 1,
                                              (m + n) // 2 + 1)) / 2


# @lc code=end
