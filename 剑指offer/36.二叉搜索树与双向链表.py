class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def help(root):
            nonlocal p
            if not root:
                return

            help(root.left)
            p.right = root
            root.left = p
            p = root
            help(root.right)

        if not root:
            return None

        new_head = Node(0)
        p = new_head
        help(root)
        new_head.right.left = p
        p.right = new_head.right
        return new_head.right
