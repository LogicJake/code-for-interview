from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def help(i, j):
            if i >= j:
                return True

            p = i
            while postorder[p] < postorder[j]:
                p += 1
            m = p
            while postorder[p] > postorder[j]:
                p += 1
            return p == j and help(i, m - 1) and help(m, j - 1)

        return help(0, len(postorder) - 1)
