#
# @lc app=leetcode.cn id=992 lang=python3
#
# [992] K 个不同整数的子数组
#

# @lc code=start
from typing import List


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def help(A, K):
            left = 0
            right = 0
            ans = 0
            mem = [0] * (len(A) + 1)
            cnt = 0

            while right < len(A):
                if mem[A[right]] == 0:
                    cnt += 1

                mem[A[right]] += 1
                right += 1

                while cnt > K:
                    mem[A[left]] -= 1
                    if mem[A[left]] == 0:
                        cnt -= 1
                    left += 1

                ans += right - left

            return ans

        return help(A, K) - help(A, K - 1)


# @lc code=end
