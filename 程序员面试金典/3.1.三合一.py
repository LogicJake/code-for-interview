class TripleInOne:
    def __init__(self, stackSize: int):
        self.stack = [0] * (3 * stackSize)
        self.top = [-1, -1, -1]
        self.cap = stackSize

    def push(self, stackNum: int, value: int) -> None:
        if self.top[stackNum] < self.cap - 1:
            self.top[stackNum] += 1
            self.stack[stackNum * self.cap + self.top[stackNum]] = value

    def pop(self, stackNum: int) -> int:
        if self.top[stackNum] == -1:
            return -1
        else:
            value = self.stack[stackNum * self.cap + self.top[stackNum]]
            self.top[stackNum] -= 1
            return value

    def peek(self, stackNum: int) -> int:
        if self.top[stackNum] == -1:
            return -1
        else:
            value = self.stack[stackNum * self.cap + self.top[stackNum]]
            return value

    def isEmpty(self, stackNum: int) -> bool:
        if self.top[stackNum] == -1:
            return True
        else:
            return False


# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)