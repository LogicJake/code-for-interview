# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> ListNode:
        p = headA
        q = headB

        while p != q:
            if not p:
                p = headB
            else:
                p = p.next
            if not q:
                q = headA
            else:
                q = q.next

        return p
