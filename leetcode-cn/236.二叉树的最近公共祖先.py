#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def dfs(self, root, fa):
#         if root.left is not None:
#             fa[root.left.val] = root
#             self.dfs(root.left, fa)

#         if root.right is not None:
#             fa[root.right.val] = root
#             self.dfs(root.right, fa)

#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
#                              q: 'TreeNode') -> 'TreeNode':
#         fa = {}
#         fa[root.val] = None
#         visited = {}
#         self.dfs(root, fa)

#         while p is not None:
#             visited[p.val] = True
#             p = fa[p.val]

#         while q is not None:
#             if q.val in visited and visited[q.val]:
#                 return q
#             q = fa[q.val]


class Solution:
    def dfs(self, root, p, q):
        if root is None:
            return False
        lson = self.dfs(root.left, p, q)
        rson = self.dfs(root.right, p, q)

        if lson and rson or ((root.val == p.val or root.val == q.val) and
                             (lson or rson)):
            self.ans = root

        return lson or rson or root.val == p.val or root.val == q.val

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        self.dfs(root, p, q)
        return self.ans


# @lc code=end
