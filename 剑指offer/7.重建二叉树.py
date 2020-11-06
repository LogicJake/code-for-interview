from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        pos_map = {}
        for i, val in enumerate(inorder):
            pos_map[val] = i

        def help(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None

            root_val = preorder[preorder_left]
            root = TreeNode(root_val)

            index = pos_map[root_val]

            root.left = help(preorder_left + 1,
                             index - inorder_left + preorder_left,
                             inorder_left, index - 1)
            root.right = help(index - inorder_left + preorder_left + 1,
                              preorder_right, index + 1, inorder_right)

            return root

        n = len(inorder)
        return help(0, n - 1, 0, n - 1)
