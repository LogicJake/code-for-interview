#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#

# @lc code=start
from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        nums1 = []
        nums2 = []

        for num in A:
            if num % 2 == 0:
                nums1.append(num)
            else:
                nums2.append(num)

        ans = []
        for i in range(len(nums1)):
            ans.append(nums1[i])
            ans.append(nums2[i])

        return ans


# @lc code=end
