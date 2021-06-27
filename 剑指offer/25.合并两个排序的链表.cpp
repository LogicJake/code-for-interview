#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x)
        : val(x)
        , next(NULL)
    {
    }
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2)
    {
        ListNode* p1 = l1;
        ListNode* p2 = l2;

        ListNode* new_head = new ListNode(0);
        ListNode* p = new_head;

        while (p1 && p2) {
            if (p1->val < p2->val) {
                p->next = p1;
                p1 = p1->next;
                p = p->next;
            } else {
                p->next = p2;
                p2 = p2->next;
                p = p->next;
            }
        }

        if (p1) {
            p->next = p1;
        }

        if (p2) {
            p->next = p2;
        }

        return new_head->next;
    }
};