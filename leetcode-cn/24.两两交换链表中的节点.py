#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        new_head = ListNode(0)
        new_head.next = head

        pre = new_head
        p = pre.next
        q = p.next

        while p is not None and q is not None:
            next = q.next

            pre.next = q
            q.next = p
            p.next = next

            pre = p
            p = next
            if p is not None:
                q = p.next
            else:
                q = None

        return new_head.next


# @lc code=end
