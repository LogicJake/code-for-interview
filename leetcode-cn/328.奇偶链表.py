#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        even_head = head.next

        odd = head
        even = even_head

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = odd.next

        odd.next = even_head
        return head


# @lc code=end
