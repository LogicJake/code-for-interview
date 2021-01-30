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
        while queue:
            tmp = []
            for _ in range(len(queue)):
                cur = queue.pop(0)
                tmp.append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            ans.append(tmp)

        return ans
