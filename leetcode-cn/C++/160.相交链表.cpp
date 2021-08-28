/*
 * @lc app=leetcode.cn id=160 lang=cpp
 *
 * [160] 相交链表
 */

// @lc code=start
#include <iostream>

using namespace std;

// struct ListNode
// {
//     int val;
//     ListNode *next;
//     ListNode(int x) : val(x), next(NULL) {}
// };

class Solution
{
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB)
    {
        ListNode *p = headA;
        ListNode *q = headB;

        while (p != q)
        {
            if (p != nullptr)
            {
                p = p->next;
            }
            else
            {
                p = headB;
            }

            if (q != nullptr)
            {
                q = q->next;
            }
            else
            {
                q = headA;
            }
        }

        return p;
    }
};
// @lc code=end
