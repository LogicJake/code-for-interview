#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None

        p = head
        n = 1

        while p.next:
            n += 1
            p = p.next

        p.next = head

        k = k % n
        k = n - k - 1

        p = head
        for _ in range(k):
            p = p.next
        new_head = p.next
        p.next = None
        return new_head


# @lc code=end
