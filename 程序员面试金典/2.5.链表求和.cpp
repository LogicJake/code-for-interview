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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
    {
        ListNode* p = l1;
        ListNode* q = l2;
        ListNode* new_head = new ListNode(0);
        ListNode* cur = new_head;
        int carry = 0;

        while (p || q || carry != 0) {
            int val = 0;

            if (p) {
                val += p->val;
                p = p->next;
            }
            if (q) {
                val += q->val;
                q = q->next;
            }
            if (carry != 0) {
                val += carry;
            }

            ListNode* node = new ListNode(val % 10);
            cur->next = node;
            cur = cur->next;
            carry = val / 10;
        }

        return new_head->next;
    }
};