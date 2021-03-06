#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []

        pre = None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            # 没有右子树或者右子树已经被访问过
            if not root.right or root.right == pre:
                ans.append(root.val)
                pre = root
                root = None
            else:
                stack.append(root)
                root = root.right

        return ans


# @lc code=end
