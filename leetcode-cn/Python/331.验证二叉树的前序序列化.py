#
# @lc app=leetcode.cn id=331 lang=python3
#
# [331] 验证二叉树的前序序列化
#


# @lc code=start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1

        for node in preorder.split(','):
            slots -= 1

            if slots < 0:
                return False

            if node != '#':
                slots += 2

        return slots == 0


# @lc code=end
