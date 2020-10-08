# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        new_head = ListNode(0)

        while pHead is not None:
            a = pHead
            pHead = pHead.next

            a.next = new_head.next
            new_head.next = a

        return new_head.next
