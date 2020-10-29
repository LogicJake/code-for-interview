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
        def swap(head, tail):
            p = head
            pre = tail.next
            while pre != tail:
                next = p.next
                p.next = pre
                pre = p
                p = next

            return tail, head

        new_head = ListNode(0)
        new_head.next = head

        pre = new_head
        head = pre.next
        tail = pre

        while True:
            num = 0
            while num < k and tail is not None:
                tail = tail.next
                num += 1
                if tail is None:
                    return new_head.next

            nex = tail.next

            head, tail = swap(head, tail)

            pre.next = head
            tail.next = nex

            pre = tail
            head = pre.next

        return new_head.next


# @lc code=end
