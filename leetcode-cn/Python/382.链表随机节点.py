#
# @lc app=leetcode.cn id=382 lang=python3
#
# [382] 链表随机节点
#

# @lc code=start
# Definition for singly-linked list.
import random


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        head = self.head
        ans = 0
        cnt = 0

        while head:
            cnt += 1

            index = random.randint(0, cnt - 1)
            if index == 0:
                ans = head.val

            head = head.next

        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end
