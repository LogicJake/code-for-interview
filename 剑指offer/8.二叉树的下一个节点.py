class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        if pNode is None:
            return None

        if pNode.right:
            pRight = pNode.right

            while pRight.left:
                pRight = pRight.left

            return pRight
        elif pNode.next is not None:
            pParent = pNode.next
            pCur = pNode

            while pParent is not None and pCur == pParent.right:
                pCur = pParent
                pParent = pParent.next

            return pParent
        return None
