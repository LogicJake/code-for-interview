class Solution {
public:
    ListNode* partition(ListNode* head, int x)
    {
        ListNode* p1 = new ListNode(0);
        ListNode* p2 = new ListNode(0);

        ListNode* q1 = p1;
        ListNode* q2 = p2;

        while (head) {
            if (head->val < x) {
                q1->next = head;
                q1 = q1->next;
            } else {
                q2->next = head;
                q2 = q2->next;
            }
            head = head->next;
        }

        q2->next = NULL;
        q1->next = p2->next;
        return p1->next;
    }
};