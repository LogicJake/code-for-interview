#
# @lc app=leetcode.cn id=995 lang=python3
#
# [995] K 连续位的最小翻转次数
#

# @lc code=start
from typing import List
from collections import deque


class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        N = len(A)
        que = deque()
        res = 0

        for i in range(N):
            if que and i >= que[0] + K:
                que.popleft()

            if len(que) % 2 == A[i]:
                if i + K > N:
                    return -1

                res += 1
                que.append(i)

        return res


# @lc code=end
