#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = [root]
        ans = []

        while queue:
            num = len(queue)

            max_ = float('-inf')
            for _ in range(num):
                node = queue.pop(0)
                max_ = max(max_, node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            ans.append(max_)

        return ans


# @lc code=end
