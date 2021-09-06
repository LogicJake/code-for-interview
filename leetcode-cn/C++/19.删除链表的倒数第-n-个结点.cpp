/*
 * @lc app=leetcode.cn id=19 lang=cpp
 *
 * [19] 删除链表的倒数第N个节点
 */

// @lc code=start
#include <iostream>
using namespace std;

// struct ListNode
// {
//     int val;
//     ListNode *next;
//     ListNode(int x)
//         : val(x), next(NULL)
//     {
//     }
// };

class Solution
{
public:
    ListNode *removeNthFromEnd(ListNode *head, int n)
    {
        ListNode *fast = new ListNode(0);
        ListNode *slow = new ListNode(0);
        ListNode *new_head = new ListNode(0);
        new_head->next = head;

        fast->next = new_head;
        slow->next = new_head;

        for (int i = 0; i < n; i++)
        {
            fast = fast->next;
        }

        while (fast->next != nullptr)
        {
            slow = slow->next;
            fast = fast->next;
        }

        slow->next = slow->next->next;

        return new_head->next;
    }
};
// @lc code=end
