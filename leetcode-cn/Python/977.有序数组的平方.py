#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = []
        for num in A:
            ans.append(num**2)
        return sorted(ans)


# @lc code=end
