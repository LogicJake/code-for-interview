#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ht = set()

        for num in nums1:
            ht.add(num)

        ans = set()
        for num in nums2:
            if num in ht:
                ans.add(num)

        return list(ans)


# @lc code=end
