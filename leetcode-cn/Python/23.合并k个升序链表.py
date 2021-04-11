#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import List


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

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        if left > right:
            return None

        mid = (left + right) >> 1
        left_list = self.merge(lists, left, mid)
        right_list = self.merge(lists, mid + 1, right)

        return self.mergeTwoLists(left_list, right_list)

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.merge(lists, 0, len(lists) - 1)


# @lc code=end
