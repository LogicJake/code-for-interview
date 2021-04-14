#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt = defaultdict(int)

        for num in nums1:
            cnt[num] += 1

        ans = []
        for num in nums2:
            if cnt[num] > 0:
                ans.append(num)
                cnt[num] -= 1

        return ans


# @lc code=end
