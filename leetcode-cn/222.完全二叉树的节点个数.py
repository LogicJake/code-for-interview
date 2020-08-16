#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def countNodes(self, root: TreeNode) -> int:
#         if root is None:
#             return 0

#         return 1 + self.countNodes(root.right) + self.countNodes(root.left)


class Solution:
    def countNodes(self, root):
        result = 0

        q = Queue()
        if root is not None:
            q.put(root)
        while not q.empty():
            tmp = q.get()
            if tmp is not None:
                result += 1
                q.put(tmp.left)
                q.put(tmp.right)

        return result


# @lc code=end
