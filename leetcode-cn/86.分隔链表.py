#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small_head = ListNode(0)
        small = small_head

        large_head = ListNode(0)
        large = large_head

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next

            head = head.next

        large.next = None
        small.next = large_head.next

        return small_head.next


# @lc code=end
