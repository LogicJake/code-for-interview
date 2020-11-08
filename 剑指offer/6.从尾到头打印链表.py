from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head)
            head = head.next

        ans = []
        while stack:
            node = stack.pop()
            ans.append(node.val)

        return ans
