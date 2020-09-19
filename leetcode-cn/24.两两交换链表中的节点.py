#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        ans = ListNode(-1)
        ans.next = head
        p = ans
        q = p.next
        r = q.next

        while p and q and r:
            p.next = r
            q.next = r.next
            r.next = q

            p = q
            if p:
                q = p.next
            else:
                q = None

            if q:
                r = q.next
            else:
                r = None

        return ans.next


# @lc code=end
