class Solution:
    def lowestCommonAncestor(self, root, o1, o2):
        if not root or root.val == o2 or root.val == o1:
            return root.val
        left = self.lowestCommonAncestor(root.left, o1, o2)
        right = self.lowestCommonAncestor(root.right, o1, o2)
        if not left:
            return right
        if not right:
            return left
        return root.val
