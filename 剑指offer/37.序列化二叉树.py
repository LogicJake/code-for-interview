# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'

        queue = [root]
        ans = []
        while queue:
            cur = queue.pop(0)
            if cur:
                ans.append(str(cur.val))
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                ans.append('null')

        return '[' + ','.join(ans) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None

        vals = data[1:-1].split(',')
        i = 1

        root = TreeNode(int(vals[0]))
        queue = [root]

        while queue:
            cur = queue.pop(0)
            if vals[i] != 'null':
                cur.left = TreeNode(int(vals[i]))
                queue.append(cur.left)
            i += 1

            if vals[i] != 'null':
                cur.right = TreeNode(int(vals[i]))
                queue.append(cur.right)

            i += 1

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))