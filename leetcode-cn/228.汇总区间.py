#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        result = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                end = nums[i - 1]

                if start == end:
                    result.append(str(start))
                else:
                    result.append('{}->{}'.format(start, end))

                start = nums[i]

        end = nums[-1]
        if start == end:
            result.append(str(start))
        else:
            result.append('{}->{}'.format(start, end))

        return result


# @lc code=end
