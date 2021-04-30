/*
 * @lc app=leetcode.cn id=24 lang=cpp
 *
 * [24] 两两交换链表中的节点
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head)
    {
        ListNode* new_head = new ListNode(0);
        new_head->next = head;
        ListNode* cur = new_head;

        while (cur->next && cur->next->next) {
            ListNode* node1 = cur->next;
            ListNode* node2 = cur->next->next;

            cur->next = node2;
            node1->next = node2->next;
            node2->next = node1;

            cur = node1;
        }

        return new_head->next;
    }
};
// @lc code=end
