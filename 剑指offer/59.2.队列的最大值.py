class MaxQueue:
    def __init__(self):
        self.que = []
        self.maxque = []

    def max_value(self) -> int:
        if self.maxque:
            return self.maxque[0]
        else:
            return -1

    def push_back(self, value: int) -> None:
        while self.maxque and self.maxque[-1] < value:
            self.maxque.pop(-1)

        self.maxque.append(value)
        self.que.append(value)

    def pop_front(self) -> int:
        if not self.que:
            return -1
        ans = self.que.pop(0)
        if ans == self.maxque[0]:
            self.maxque.pop(0)
        return ans


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()