#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []

        if not root:
            return []

        queue = [root]

        while queue:
            ans.append(queue[-1].val)

            for _ in range(len(queue)):
                root = queue.pop(0)

                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)

        return ans


# @lc code=end
