#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []

        current_node = head
        while current_node is not None:
            nums.append(current_node.val)
            current_node = current_node.next

        for i in range(len(nums)):
            j = len(nums) - i - 1
            if nums[i] != nums[j]:
                return False

        return True


# @lc code=end
