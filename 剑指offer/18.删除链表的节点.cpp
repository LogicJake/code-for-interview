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
    ListNode* deleteNode(ListNode* head, int val)
    {
        ListNode* new_head = new ListNode();
        new_head->next = head;

        ListNode* pre = new_head;
        while (pre->next != NULL) {
            if (pre->next->val == val) {
                pre->next = pre->next->next;
                break;
            } else {
                pre = pre->next;
            }
        }

        return new_head->next;
    }
};