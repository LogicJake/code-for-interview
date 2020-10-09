#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        slow = head
        fast = slow.next

        while fast != slow:
            if slow is None or fast is None or fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

        return True


# @lc code=end
