from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        ans = []

        if not root:
            return []

        queue = [root]
        order = 0
        while queue:
            tmp = []
            for _ in range(len(queue)):
                cur = queue.pop(0)
                tmp.append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            if order % 2 == 0:
                ans.append(tmp)
            else:
                ans.append(tmp[::-1])
            order += 1

        return ans
