#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize_helper(self, root):
        if root is None:
            return 'None,'

        s = str(root.val) + ','
        s += self.serialize_helper(root.left)
        s += self.serialize_helper(root.right)

        return s

    def serialize(self, root):
        a = self.serialize_helper(root)
        return a

    def deserialize_helper(self, data):
        val = data.pop(0)
        if val == 'None':
            return None

        root = TreeNode(val)
        root.left = self.deserialize_helper(data)
        root.right = self.deserialize_helper(data)
        return root

    def deserialize(self, data):
        data = data.split(',')
        root = self.deserialize_helper(data)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end
