#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sign = 0
        ans = ListNode()
        p = ans
        while l1 is not None and l2 is not None:
            sum_ = l1.val + l2.val

            p.next = ListNode((sum_ + sign) % 10)
            sign = (sum_ + sign) // 10

            l1 = l1.next
            l2 = l2.next
            p = p.next

        while l1 is not None:
            sum_ = l1.val

            p.next = ListNode((sum_ + sign) % 10)
            sign = (sum_ + sign) // 10

            l1 = l1.next
            p = p.next

        while l2 is not None:
            sum_ = l2.val

            p.next = ListNode((sum_ + sign) % 10)
            sign = (sum_ + sign) // 10

            l2 = l2.next
            p = p.next

        if sign != 0:
            p.next = ListNode(sign)

        return ans.next


# @lc code=end
