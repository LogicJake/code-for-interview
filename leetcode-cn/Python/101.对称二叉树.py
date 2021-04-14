#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        queue = [root, root]

        while len(queue) != 0:
            u = queue.pop(0)
            v = queue.pop(0)

            if u is None and v is None:
                continue

            if u is None or v is None or u.val != v.val:
                return False

            queue.append(u.left)
            queue.append(v.right)

            queue.append(u.right)
            queue.append(v.left)

        return True


# @lc code=end
