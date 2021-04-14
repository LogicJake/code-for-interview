#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#


# @lc code=start
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        tmp_stack = []

        while self.stack:
            tmp_stack.append(self.stack.pop(-1))

        self.stack.append(x)

        while tmp_stack:
            self.stack.append(tmp_stack.pop(-1))

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop(-1)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
