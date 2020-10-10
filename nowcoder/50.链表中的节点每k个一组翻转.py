class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse(self, head, tail):
        pre = tail.next

        p = head
        while pre != tail:
            next = p.next

            p.next = pre
            pre = p

            p = next

        return tail, head

    def reverseKGroup(self, head, k):
        new_head = ListNode(0)
        new_head.next = head

        pre = new_head

        while head is not None:
            tail = pre

            for _ in range(k):
                tail = tail.next
                if tail is None:
                    return new_head.next

            next = tail.next

            head, tail = self.reverse(head, tail)
            pre.next = head
            tail.next = next

            head = next
            pre = tail

        return new_head.next