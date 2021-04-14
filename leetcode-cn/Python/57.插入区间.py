#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        place = False
        ans = []
        for l, r in intervals:
            if r < left:
                ans.append([l, r])
            elif l > right:
                if not place:
                    ans.append([left, right])
                    place = True
                ans.append([l, r])
            else:
                left = min(left, l)
                right = max(right, r)

        if not place:
            ans.append([left, right])
        return ans


# @lc code=end
