#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        slow = head
        fast = head

        while slow is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                ptr = head

                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr

        return None


# @lc code=end
