#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
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
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []

        queue = [root]
        cnt = 1
        result = []
        while len(queue) != 0:
            new_cnt = 0
            avg = 0

            count = cnt
            while cnt != 0:
                node = queue.pop(0)
                avg += node.val

                if node.left:
                    queue.append(node.left)
                    new_cnt += 1
                if node.right:
                    queue.append(node.right)
                    new_cnt += 1

                cnt -= 1
            avg = avg / count

            result.append(avg)
            cnt = new_cnt

        return result


# @lc code=end
