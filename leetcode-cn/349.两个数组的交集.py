#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        t = set()

        for num in nums1:
            t.add(num)

        ans = set()
        for num in nums2:
            if num in t:
                ans.add(num)

        return list(ans)


# @lc code=end
