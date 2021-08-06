/*
 * @lc app=leetcode.cn id=24 lang=cpp
 *
 * [24] 两两交换链表中的节点
 */

// @lc code=start
// struct ListNode {
//     int val;
//     ListNode* next;
//     ListNode(int x)
//         : val(x)
//         , next(NULL)
//     {
//     }
// };

class Solution {
public:
    ListNode* swapPairs(ListNode* head)
    {
        ListNode* new_head = new ListNode(0);
        new_head->next= head;
        ListNode* cur = new_head;

        while (cur && cur->next && cur->next->next)
        {
            ListNode* p = cur->next;
            ListNode* q = p->next;

            p->next = q->next;
            q->next = p;
            cur->next = q;

            cur = p;
        }
        

        return new_head->next;
    }
};
// @lc code=end
