# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        ans = None

        def help(root):
            nonlocal k, ans
            if ans or not root:
                return

            help(root.right)
            if not ans and k == 1:
                ans = root.val
            else:
                k -= 1
            help(root.left)

        help(root)
        return ans
