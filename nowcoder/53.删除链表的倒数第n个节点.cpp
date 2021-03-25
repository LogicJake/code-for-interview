struct ListNode {
    int val;
    struct ListNode* next;
};

class Solution {
public:
    /**
     * 
     * @param head ListNode类 
     * @param n int整型 
     * @return ListNode类
     */
    ListNode* removeNthFromEnd(ListNode* head, int n)
    {
        ListNode* new_head = new ListNode(0);
        new_head->next = head;

        ListNode* fast = new_head;
        ListNode* slow = new_head;

        while (n > 0) {
            fast = fast->next;
            n -= 1;
        }

        while (fast->next) {
            slow = slow->next;
            fast = fast->next;
        }

        ListNode* tmp = slow->next;
        slow->next = slow->next->next;
        delete tmp;

        return new_head->next;
    }
};