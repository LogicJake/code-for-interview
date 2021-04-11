#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        new_head = ListNode(0)

        p = head
        while p:
            next = p.next

            q = new_head
            while q.next and q.next.val < p.val:
                q = q.next
            p.next = q.next
            q.next = p

            p = next

        return new_head.next


# @lc code=end
