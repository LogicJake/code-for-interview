#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        order = 1
        queue = [root]
        ans = []
        while queue:
            sz = len(queue)

            tmp = []
            for _ in range(sz):
                cur = queue.pop(0)
                tmp.append(cur.val)

                if cur.left:
                    queue.append(cur.left)

                if cur.right:
                    queue.append(cur.right)
            if order % 2 == 0:
                ans.append(tmp[::-1])
            else:
                ans.append(tmp)
            order = order + 1

        return ans


# @lc code=end
