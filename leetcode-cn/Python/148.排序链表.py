#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slow = head.next
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        left = head
        slow.next = None

        print(left, right)

        left = self.sortList(left)
        right = self.sortList(right)

        new_head = ListNode(0)
        p = new_head

        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next

            p = p.next

        if left:
            p.next = left

        if right:
            p.next = right

        return new_head.next


# @lc code=end
