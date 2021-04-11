#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ans = None

        def help(root):
            nonlocal ans, k
            if not root or ans:
                return

            help(root.left)
            k -= 1
            if k == 0:
                ans = root.val
            help(root.right)

        help(root)
        return ans


# @lc code=end
