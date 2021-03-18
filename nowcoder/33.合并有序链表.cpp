struct ListNode {
    int val;
    struct ListNode* next;
};

class Solution {
public:
    /**
     * 
     * @param l1 ListNode类 
     * @param l2 ListNode类 
     * @return ListNode类
     */
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2)
    {
        ListNode* new_head = new ListNode;
        ListNode* p = new_head;

        while (l1 && l2) {
            if (l1->val <= l2->val) {
                p->next = l1;
                l1 = l1->next;
            } else {
                p->next = l2;
                l2 = l2->next;
            }

            p = p->next;
        }

        if (l1) {
            p->next = l1;
        }

        if (l2) {
            p->next = l2;
        }

        return new_head->next;
    }
};