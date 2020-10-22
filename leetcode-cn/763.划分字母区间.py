#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {}

        for i, c in enumerate(S):
            last[c] = i

        start = 0
        end = 0
        ans = []
        for i, c in enumerate(S):
            end = max(end, last[c])

            if end == i:
                ans.append(end - start + 1)
                start = end + 1

        return ans


# @lc code=end
