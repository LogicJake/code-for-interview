# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ans = []

        if not head:
            return True

        while head:
            ans.append(head)
            head = head.next

        i = 0
        j = len(ans) - 1

        while i <= j:
            if ans[i].val != ans[j].val:
                return False

            i += 1
            j -= 1
        return True
