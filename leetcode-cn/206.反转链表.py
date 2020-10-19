#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = ListNode(0)

        p = head
        while p is not None:
            q = p.next
            p.next = new_head.next
            new_head.next = p

            p = q

        return new_head.next


# @lc code=end
