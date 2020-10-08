#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        if len(intervals) <= 1:
            return intervals
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            tmp = ans.pop()
            if tmp[1] >= intervals[i][0]:
                if tmp[1] >= intervals[i][1]:
                    ans.append(tmp)
                else:
                    ans.append([tmp[0], intervals[i][1]])
            else:
                ans.append(tmp)
                ans.append(intervals[i])
        return ans


# @lc code=end
