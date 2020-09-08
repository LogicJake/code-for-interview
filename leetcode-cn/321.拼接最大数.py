#
# @lc app=leetcode.cn id=321 lang=python3
#
# [321] 拼接最大数
#

# @lc code=start
from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int],
                  k: int) -> List[int]:
        def maxSub(num, k):
            if k >= len(num):
                return num

            res = []
            pop_cnt = len(num) - k

            for n in num:
                while len(res) > 0 and n > res[-1] and pop_cnt > 0:
                    res.pop()
                    pop_cnt -= 1

                res.append(n)

            return res[:k]

        def merge(sub1_, sub2_):
            sub1 = sub1_.copy()
            sub2 = sub2_.copy()

            res = []
            while len(sub1) > 0 and len(sub2) > 0:
                if sub1 > sub2:
                    res.append(sub1.pop(0))
                elif sub2 > sub1:
                    res.append(sub2.pop(0))
                else:
                    break

            res += sub1 + sub2

            return res

        max_num = []
        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                sub1 = maxSub(nums1, i)
                sub2 = maxSub(nums2, k - i)

                tmp = merge(sub1, sub2)

                if tmp > max_num:
                    max_num = tmp

        return max_num


# [2,5,6,4,4,0]\n[7,3,8,0,6,5,7,6,2]\n15
# @lc code=end
