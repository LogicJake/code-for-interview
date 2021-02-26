#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        fast = head
        slow = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if not slow or not fast:
                return None

            if slow == fast:
                p = head

                while p != fast:
                    p = p.next
                    fast = fast.next

                return p

        return None


# @lc code=end
