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

        pre = new_head
        tail = new_head

        def swap(head, tail):
            prev = None
            p = head

            while prev != tail:
                nex = p.next
                p.next = prev
                prev = p
                p = nex

            return tail, head

        while True:
            cnt = 0

            while cnt < k and tail is not None:
                tail = tail.next
                cnt += 1

                if tail is None:
                    return new_head.next

            next = tail.next
            head, tail = swap(head, tail)

            pre.next = head
            tail.next = next

            pre = tail
            head = next


# @lc code=end
