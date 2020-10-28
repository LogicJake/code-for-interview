#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#

# @lc code=start
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if len(arr) == 0:
            return True

        cnt = {}
        for num in arr:
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1

        cnts = list(cnt.values())
        cnts.sort()

        for i in range(1, len(cnts)):
            if cnts[i] == cnts[i - 1]:
                return False

        return True


# @lc code=end
