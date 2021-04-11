#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        new_head = ListNode(0, head)
        cur = new_head

        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                cur = cur.next
                x = cur.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return new_head.next


# @lc code=end
