class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_head = ListNode(0)
        r = new_head

        p = l1
        q = l2

        while p and q:
            while p and q and p.val <= q.val:
                next = p.next

                p.next = r.next
                r.next = p

                r = p
                p = next

            while p and q and q.val <= p.val:
                next = q.next

                q.next = r.next
                r.next = q

                r = q
                q = next

        if q:
            r.next = q

        if p:
            r.next = p

        return new_head.next
