#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        order = 0

        if not root:
            return []

        ans = []
        queue = [root]
        while queue:
            tmp = []
            for _ in range(len(queue)):
                root = queue.pop(0)
                tmp.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)

            if order % 2 == 0:
                ans.append(tmp)
            else:
                ans.append(tmp[::-1])
            order += 1

        return ans


# @lc code=end
