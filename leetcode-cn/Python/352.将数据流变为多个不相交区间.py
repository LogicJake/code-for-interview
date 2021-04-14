#
# @lc app=leetcode.cn id=352 lang=python3
#
# [352] 将数据流变为多个不相交区间
#

# @lc code=start
from typing import List


class SummaryRanges:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []

    def addNum(self, val: int) -> None:
        if val not in self.values:
            self.values.append(val)

    def getIntervals(self) -> List[List[int]]:
        res = []
        ret = sorted(self.values)
        start = ret[0]
        end = ret[0]
        n = len(ret)
        for i in range(1, n):
            if ret[i] - ret[i - 1] == 1:
                end = ret[i]
            else:
                res.append([start, end])
                start = ret[i]
                end = ret[i]
        res.append([start, end])
        return res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
# @lc code=end
