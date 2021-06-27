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
    ListNode* getKthFromEnd(ListNode* head, int k)
    {
        ListNode* slow = head;
        ListNode* fast = head;

        for (int i = 0; i < k; i++) {
            fast = fast->next;
        }

        while (fast != NULL) {
            slow = slow->next;
            fast = fast->next;
        }

        return slow;
    }
};