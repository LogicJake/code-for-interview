# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def help(left, right):
            if not left and not right:
                return True

            if not left or not right or left.val != right.val:
                return False

            return help(left.left, right.right) and help(
                left.right, right.left)

        if not root:
            return True

        return help(root.left, root.right)
