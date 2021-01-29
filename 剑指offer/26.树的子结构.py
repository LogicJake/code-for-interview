# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def dfs(t1, t2):
            # 如果 B 已经遍历完了，true
            if not t2:
                return True
            # 如果 B 还有，但 A 遍历完了，那 B 剩下的就没法匹配了，false
            if not t1:
                return False
            # 不相等，false
            if t1.val != t2.val:
                return False

            return dfs(t1.left, t2.left) and dfs(t1.right, t2.right)

        if not A or not B:
            return False

        res = False

        # 如果在 A 中匹配到了与 B 的根节点的值一样的节点
        if A.val == B.val:
            res = dfs(A, B)

        # 如果匹配不到，A 往左
        if not res:
            res = self.isSubStructure(A.left, B)

        # 还匹配不到，A 往右
        if not res:
            res = self.isSubStructure(A.right, B)

        return res
