# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_head = ListNode(0)
        p = new_head

        flag = 0

        while l1 and l2:
            total = l1.val + l2.val + flag
            flag = total // 10
            val = total % 10

            node = ListNode(val)
            p.next = node
            p = p.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            total = l1.val + flag
            flag = total // 10
            val = total % 10

            node = ListNode(val)
            p.next = node
            p = p.next

            l1 = l1.next

        while l2:
            total = l2.val + flag
            flag = total // 10
            val = total % 10

            node = ListNode(val)
            p.next = node
            p = p.next

            l2 = l2.next

        if flag:
            node = ListNode(flag)
            p.next = node
            p = p.next

        return new_head.next
