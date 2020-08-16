#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start


class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        tmp = [x]

        while len(self.stack) != 0:
            tmp.append(self.stack.pop(0))

        self.stack = tmp

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.stack.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return False if len(self.stack) != 0 else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
