#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 先分割成两个链表
        if not head or not head.next:
            return
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None

        # 后面一个链表倒序
        pre = None
        cur = head2

        while cur:
            next = cur.next
            cur.next = pre

            pre = cur
            cur = next

        head2 = pre

        # 插入第一个链表
        p = head

        while p and head2:
            q = p.next

            p.next = head2
            next = head2.next
            head2.next = q
            head2 = next

            p = q


# @lc code=end
