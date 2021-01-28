# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p = head
        q = p
        for _ in range(k):
            q = q.next

        while q:
            q = q.next
            p = p.next

        return p
