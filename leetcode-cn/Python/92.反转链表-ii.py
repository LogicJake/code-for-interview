#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int,
                       right: int) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head

        pre = new_head
        tail = head

        def reverse(head, tail):
            pre = tail.next
            p = head

            while pre != tail:
                next = p.next
                p.next = pre
                pre = p
                p = next

            return tail, head

        i = 1
        j = 1

        while i < left or j < right:
            if i < left:
                pre = head
                head = head.next
                i += 1

            tail = tail.next
            j += 1

        print(head.val, tail.val)

        next = tail.next
        head, tail = reverse(head, tail)
        pre.next = head
        tail.next = next

        return new_head.next


# @lc code=end
