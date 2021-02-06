class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def help(root):
            nonlocal pre, head
            if not root:
                return

            help(root.left)

            if pre:
                pre.right = root
                root.left = pre
            else:
                print(root.val)
                head = root

            pre = root

            help(root.right)

        head = None
        pre = None

        if not root:
            return None
        help(root)

        head.left = pre
        pre.right = head

        return head
