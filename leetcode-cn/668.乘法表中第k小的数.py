#
# @lc app=leetcode.cn id=668 lang=python3
#
# [668] 乘法表中第k小的数
#

# @lc code=start
import heapq


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def help(m, n, num):
            cnt = 0

            for i in range(1, m + 1):
                cnt += min(n, num // i)

            return cnt

        left = 1
        right = m * n

        while left < right:
            mid = (left + right) // 2
            cnt = help(m, n, mid)

            if cnt < k:
                left = mid + 1
            else:
                right = mid

        return left


# @lc code=end
