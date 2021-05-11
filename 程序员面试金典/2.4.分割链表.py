# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = ListNode(0)
        big = ListNode(0)

        p = small
        q = big

        while head:
            if head.val < x:
                p.next = head
                p = p.next
            else:
                q.next = head
                q = q.next

            head = head.next

        # 这一步最重要，要不然链表无法结束
        q.next = None
        p.next = big.next
        return small.next
