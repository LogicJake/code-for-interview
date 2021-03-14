#include <iostream>

struct ListNode {
    int val;
    struct ListNode* next;
    ListNode(int x)
        : val(x)
        , next(NULL)
    {
    }
};

class Solution {
public:
    ListNode* ReverseList(ListNode* pHead)
    {
        if (pHead == NULL) {
            return NULL;
        }

        ListNode* pre = NULL;
        ListNode* p = pHead;

        while (p) {
            ListNode* next = p->next;
            p->next = pre;

            pre = p;
            p = next;
        }
        return pre;
    }
};