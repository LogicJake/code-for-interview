#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
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
    def findMode(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return []

        max_count = -1
        count = 0
        num = -1

        def help(root):
            nonlocal ans
            nonlocal max_count
            nonlocal count
            nonlocal num

            if not root:
                return

            help(root.left)

            if root.val != num:
                if num != -1:
                    if count > max_count:
                        max_count = count
                        ans = [num]
                    elif count == max_count:
                        ans.append(num)
                    num = root.val
                    count = 1
                else:
                    num = root.val
                    count = 1
            else:
                count += 1

            help(root.right)

        help(root)

        if count > max_count:
            max_count = count
            ans = [num]
        elif count == max_count:
            ans.append(num)

        return ans


# @lc code=end
