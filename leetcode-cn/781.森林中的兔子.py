#
# @lc app=leetcode.cn id=781 lang=python3
#
# [781] 森林中的兔子
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = defaultdict(int)
        for num in answers:
            cnt[num] += 1

        ans = 0
        for k, v in cnt.items():
            ans += (k + 1) * ((v + k) // (k + 1))
        return ans


# @lc code=end
