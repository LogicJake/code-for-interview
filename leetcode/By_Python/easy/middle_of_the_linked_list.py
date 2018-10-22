# -*- coding: utf-8 -*-
# @Time    : 18-10-22 下午2:01
# @Author  : LogicJake
# @File    : middle_of_the_linked_list.py


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        num = 0
        i = head
        while i != None:
            num += 1
            i = i.next

        target = num // 2
        i = head
        j = 0
        while i != None:
            if j == target:
                return i
            j += 1
            i = i.next
