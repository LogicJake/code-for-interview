#
# @lc app=leetcode.cn id=327 lang=python3
#
# [327] 区间和的个数
#

# @lc code=start
from typing import List
import itertools


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        presum = [0] + list(itertools.accumulate(nums))  # 前缀和数组

        def merge(left, right):
            if right == left:
                return 0
            mid = (left + right) >> 1
            return merge(left, mid) + merge(mid + 1, right) + merge_sort(
                left, mid, right)

        def merge_sort(left, mid, right):  # 返回排序过程中检测到的可行组合数
            nonlocal presum

            # -- cal $l & $r -- #
            p = left
            l = r = mid + 1
            ret = 0  # 区段统计标志
            while p <= mid:
                while l <= right and presum[l] - presum[p] < lower:
                    l += 1
                while r <= right and presum[r] - presum[p] <= upper:
                    r += 1
                ret += (r - l)
                p += 1
            # --END-- #

            # -- do sort from here -- #
            p1, p2 = left, mid + 1
            temp = []  # length is {right-left+1}
            while p1 <= mid or p2 <= right:
                if p1 > mid:
                    temp.append(presum[p2])
                    p2 += 1
                elif p2 > right:
                    temp.append(presum[p1])
                    p1 += 1
                else:
                    if presum[p1] < presum[p2]:
                        temp.append(presum[p1])
                        p1 += 1
                    else:
                        temp.append(presum[p2])
                        p2 += 1
            presum[left:right + 1] = temp  # copy
            # -- sort END -- #
            return ret

        return merge(0, len(presum) - 1)


# @lc code=end
