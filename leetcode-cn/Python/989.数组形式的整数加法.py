#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 数组形式的整数加法
#

# @lc code=start
from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        ans = A[::-1]
        flag = K

        for i in range(len(ans)):
            tmp = ans[i] + flag
            ans[i] = tmp % 10
            flag = tmp // 10

        while flag:
            ans.append(flag % 10)
            flag = flag // 10

        return ans[::-1]


# @lc code=end
