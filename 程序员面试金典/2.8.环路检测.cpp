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
    ListNode* detectCycle(ListNode* head)
    {
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* p = head;

        while (slow && fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;

            if (slow == fast) {
                while (p != slow) {
                    slow = slow->next;
                    p = p->next;
                }
                return p;
            }
        }
        return NULL;
    }
};