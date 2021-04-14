#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2

        new_head = ListNode(0)
        r = new_head

        while p and q:
            if p.val < q.val:
                r.next = p
                r = r.next
                p = p.next

            else:
                r.next = q
                r = r.next
                q = q.next

        if p:
            r.next = p
        if q:
            r.next = q

        return new_head.next


# @lc code=end
