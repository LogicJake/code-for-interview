import heapq


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # 小顶堆存储较大的数
        self.lager = []
        # 大顶堆存储较小的数
        self.smaller = []

    def addNum(self, num: int) -> None:
        if len(self.lager) != len(self.smaller):
            heapq.heappush(self.lager, num)
            heapq.heappush(self.smaller, heapq.heappop(self.lager))
        else:
            heapq.heappush(self.smaller, num)
            heapq.heappush(self.lager, heapq.heappop(self.smaller))

    def findMedian(self) -> float:
        if len(self.lager) != len(self.smaller):
            return self.lager[0]
        else:
            return (self.lager[0] + self.smaller[0]) // 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
