#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#


# @lc code=start
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.container = []
        self.cnt = 0

    def addNum(self, num: int) -> None:
        self.container.append(num)
        self.cnt += 1

    def findMedian(self) -> float:
        self.container.sort()
        if self.cnt % 2 == 0:
            a = self.cnt // 2
            b = a - 1

            return (self.container[a] + self.container[b]) / 2
        return self.container[self.cnt // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
