# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        pre = None
        while p != root:
            if p.val > root.val:
                root = root.right
            else:
                pre = root
                root = root.left

        if root.right:
            root = root.right
            while root.left:
                root = root.left

            return root

        else:
            return pre
