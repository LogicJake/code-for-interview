#include <iostream>
using namespace std;

struct ListNode {
    int val;
    struct ListNode* next;
};

class Solution {
public:
    /**
     * 
     * @param head ListNode类 
     * @param k int整型 
     * @return ListNode类
     */
    pair<ListNode*, ListNode*> reverse(ListNode* head, ListNode* tail)
    {
        ListNode* pre = NULL;
        ListNode* p = head;

        while (pre != tail) {
            ListNode* next = p->next;
            p->next = pre;
            pre = p;
            p = next;
        }
        return { tail, head };
    }

    ListNode* reverseKGroup(ListNode* head, int k)
    {
        ListNode* new_head = new ListNode(0);
        new_head->next = head;
        ListNode* pre = new_head;

        while (head != NULL) {
            ListNode* tail = pre;

            for (int i = 0; i < k; i++) {
                tail = tail->next;
                if (tail == NULL) {
                    return new_head->next;
                }
            }

            ListNode* next = tail->next;

            pair<ListNode*, ListNode*> result = reverse(head, tail);
            head = result.first;
            tail = result.second;

            pre->next = head;
            tail->next = next;
            pre = tail;
            head = next;
        }

        return new_head->next;
    }
};