#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None

        dummy = ListNode(0)
        dummy.next = head

        p1 = dummy
        for _ in range(n + 1):
            p1 = p1.next

        p2 = dummy
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next

        p2.next = p2.next.next

        return dummy.next


# @lc code=end
