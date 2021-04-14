#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        current_val = root.val

        if p.val > current_val and q.val > current_val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < current_val and q.val < current_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root


# @lc code=end
