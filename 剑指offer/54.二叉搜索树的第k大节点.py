# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        ans = []

        def help(root):
            if not root:
                return

            help(root.left)
            ans.append(root.val)
            help(root.right)

        help(root)
        return ans[-k]
