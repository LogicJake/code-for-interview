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

class Solution
{
public:
    ListNode *swapPairs(ListNode *head)
    {
        if (head == nullptr)
        {
            return head;
        }

        ListNode *new_head = new ListNode();
        new_head->next = head;

        ListNode *pre = new_head;

        while (pre->next && pre->next->next)
        {
            ListNode *p = pre->next;
            ListNode *q = pre->next->next;
            pre->next = q;
            p->next = q->next;
            q->next = p;

            pre = p;
        }

        return new_head->next;
    }
};
// @lc code=end
