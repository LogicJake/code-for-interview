#
# @lc app=leetcode.cn id=1356 lang=python3
#
# [1356] 根据数字二进制下 1 的数目排序
#
# @lc code=start

from typing import List
from collections import defaultdict


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        cnt = defaultdict(list)
        arr.sort()

        def numberOf1(n):
            count = 0
            while n != 0:
                count += 1
                n = n & (n - 1)
            return count

        for num in arr:
            num1 = numberOf1(num)
            cnt[num1].append(num)

        ans = []
        for k in sorted(cnt.keys()):
            ans += cnt[k]
        return ans


# @lc code=end
