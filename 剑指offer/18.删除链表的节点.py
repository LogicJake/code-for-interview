class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        new_head = ListNode(0)
        new_head.next = head

        p = new_head
        q = p.next

        while q:
            if q.val == val:
                p.next = q.next
                break
            else:
                p = q
                q = p.next

        return new_head.next
