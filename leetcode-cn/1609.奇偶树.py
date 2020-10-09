#
# @lc app=leetcode.cn id=1609 lang=python3
#
# [1609] 奇偶树
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if root is None:
            return False

        stack = [root]
        level = 0
        while len(stack) != 0:
            num = len(stack)

            is_odd = level % 2
            if is_odd:
                pre = 10**6 + 1
            else:
                pre = 0

            for _ in range(num):
                node = stack.pop(0)
                val = node.val

                if is_odd:
                    if val % 2 != 0:
                        return False
                    if val >= pre:
                        return False
                else:
                    if val % 2 != 1:
                        return False

                    if val <= pre:
                        return False

                pre = val

                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)

            level += 1

        return True


# @lc code=end
