#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        new_head = ListNode(0)
        p = new_head
        while left is not None and right is not None:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next

            p = p.next
        if left is not None:
            p.next = left
        else:
            p.next = right

        return new_head.next


# @lc code=end
