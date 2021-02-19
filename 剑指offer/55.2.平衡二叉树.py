class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        ans = True

        def help(root):
            nonlocal ans
            if not root:
                return 0

            left_height = help(root.left)
            right_height = help(root.right)

            if abs(left_height - right_height) > 1:
                ans = False

            return 1 + max(left_height, right_height)

        help(root)
        return ans
