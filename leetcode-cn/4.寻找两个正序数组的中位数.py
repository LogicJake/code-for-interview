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
        m = len(nums1)
        n = len(nums2)

        i = 0
        j = 0
        global_index = 0
        if (m + n) % 2 == 0:
            index1 = (m + n) // 2
            index2 = index1 - 1
            result = 0
            count = 0
            while i < m or j < n:
                if (i < m and j < n and nums1[i] < nums2[j]) or (i < m
                                                                 and j >= n):
                    if global_index == index1 or global_index == index2:
                        result += nums1[i]
                        count += 1

                        if count == 2:
                            return result / 2

                    i += 1
                    global_index += 1
                else:
                    if global_index == index1 or global_index == index2:
                        result += nums2[j]
                        count += 1

                        if count == 2:
                            return result / 2

                    j += 1
                    global_index += 1

        else:
            index = (m + n) // 2

            while i < m or j < n:
                if (i < m and j < n and nums1[i] < nums2[j]) or (i < m
                                                                 and j >= n):
                    if global_index == index:
                        return nums1[i]

                    i += 1
                    global_index += 1
                else:
                    if global_index == index:
                        return nums2[j]

                    j += 1
                    global_index += 1


# @lc code=end
