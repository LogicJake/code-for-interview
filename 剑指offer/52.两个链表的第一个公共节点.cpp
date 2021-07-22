#include <iostream>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x)
        : val(x), next(NULL)
    {
    }
};

class Solution
{
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB)
    {
        ListNode *p = headA;
        ListNode *q = headB;

        while (p != q)
        {
            if (p != NULL)
            {
                p = p->next;
            }
            else
            {
                p = headB;
            }

            if (q != NULL)
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