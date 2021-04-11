#
# @lc app=leetcode.cn id=1365 lang=python3
#
# [1365] 有多少小于当前数字的数字
#

# @lc code=start
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnt = [0] * 101

        for num in nums:
            cnt[num] += 1

        for i in range(1, 101):
            cnt[i] = cnt[i - 1] + cnt[i]

        ans = []
        for num in nums:
            if num - 1 >= 0:
                ans.append(cnt[num - 1])
            else:
                ans.append(0)
        return ans


# @lc code=end
