#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = [root]
        depth = 1

        while queue:
            sz = len(queue)

            for _ in range(sz):
                cur = queue.pop(0)
                if not cur.left and not cur.right:
                    return depth

                if cur.left:
                    queue.append(cur.left)

                if cur.right:
                    queue.append(cur.right)

            depth += 1


# @lc code=end
