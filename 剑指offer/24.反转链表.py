# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = ListNode(0)
        p = head

        while p:
            next = p.next
            p.next = new_head.next
            new_head.next = p

            p = next

        return new_head.next
