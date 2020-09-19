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
        p1 = l1
        p2 = l2

        ans = ListNode()
        q = ans

        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                q.next = p1
                q = q.next
                p1 = p1.next
            else:
                q.next = p2
                q = q.next
                p2 = p2.next

        if p1:
            q.next = p1

        if p2:
            q.next = p2

        return ans.next


# @lc code=end
