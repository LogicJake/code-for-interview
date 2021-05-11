class SortedStack:
    def __init__(self):
        self.help = []
        self.stack = []

    def push(self, val: int) -> None:
        while self.stack and val > self.stack[-1]:
            self.help.append(self.stack.pop(-1))

        self.stack.append(val)

        while self.help:
            self.stack.append(self.help.pop(-1))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop(-1)

    def peek(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return not self.stack
