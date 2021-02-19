class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def help(root):
            if not root:
                return 0

            left_height = help(root.left)
            right_height = help(root.right)

            return 1 + max(left_height, right_height)

        return help(root)
