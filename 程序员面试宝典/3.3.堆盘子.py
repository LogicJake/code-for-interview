class StackOfPlates:
    def __init__(self, cap: int):
        self.cap = cap
        self.stacks = []

    def push(self, val: int) -> None:
        if self.cap == 0:
            return
        if not self.stacks or len(self.stacks[-1]) == self.cap:
            self.stacks.append([])

        self.stacks[-1].append(val)

    def pop(self) -> int:
        if not self.stacks:
            return -1

        res = self.stacks[-1].pop(-1)
        if len(self.stacks[-1]) == 0:
            del self.stacks[-1]
        return res

    def popAt(self, index: int) -> int:
        if len(self.stacks) <= index:
            return -1

        res = self.stacks[index].pop(-1)
        if len(self.stacks[index]) == 0:
            del self.stacks[index]
        return res


# Your StackOfPlates object will be instantiated and called as such:
# obj = StackOfPlates(cap)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAt(index)