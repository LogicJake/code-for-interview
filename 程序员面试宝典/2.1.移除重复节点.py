# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head

        pre = new_head
        p = head
        mem = set()

        while p:
            if p.val in mem:
                next = p.next
                pre.next = p.next
                p = next
            else:
                mem.add(p.val)
                pre = p
                p = p.next
        return new_head.next
