#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head

        def swap(head, tail):
            pre = tail.next
            p = head
            while pre != tail:
                next = p.next

                p.next = pre
                pre = p

                p = next

            return tail, head

        pre = new_head
        tail = pre

        cnt = 0
        while tail:
            cnt += 1
            tail = tail.next

            if not tail:
                return new_head.next

            if cnt == k:
                next = tail.next
                head, tail = swap(head, tail)

                pre.next = head
                tail.next = next

                pre = tail
                head = next

                cnt = 0

        return new_head.next


# @lc code=end
