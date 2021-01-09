#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pre = -1
        cnt = 0
        m = len(flowerbed)
        for i in range(m):
            if flowerbed[i] == 1:
                if pre == -1:
                    cnt += i // 2
                else:
                    cnt += (i - pre - 2) // 2
                pre = i
                if cnt >= m:
                    return True

        if pre == -1:
            cnt += (m + 1) // 2
        else:
            cnt += (m - pre - 1) // 2

        return cnt >= n


# @lc code=end
