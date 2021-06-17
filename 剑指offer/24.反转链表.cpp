#include <iostream>

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
    ListNode* reverseList(ListNode* head)
    {
        ListNode* new_head = new ListNode();

        ListNode* p = head;

        while (p != NULL) {
            ListNode* next = p->next;

            p->next = new_head->next;
            new_head->next = p;

            p = next;
        }

        return new_head->next;
    }
};