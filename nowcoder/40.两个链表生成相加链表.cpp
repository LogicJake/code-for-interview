#include <stack>
using namespace std;

struct ListNode {
    int val;
    struct ListNode* next;
};

class Solution {
public:
    /**
     * 
     * @param head1 ListNode类 
     * @param head2 ListNode类 
     * @return ListNode类
     */
    ListNode* addInList(ListNode* head1, ListNode* head2)
    {
        stack<int> st1;
        stack<int> st2;

        while (head1) {
            st1.push(head1->val);
            head1 = head1->next;
        }

        while (head2) {
            st2.push(head2->val);
            head2 = head2->next;
        }

        int carry = 0;
        ListNode* new_head = new ListNode();
        while (!st1.empty() || !st2.empty() || carry) {
            int a = 0;
            if (!st1.empty()) {
                a = st1.top();
                st1.pop();
            }

            int b = 0;
            if (!st2.empty()) {
                b = st2.top();
                st2.pop();
            }

            int res = a + b + carry;
            carry = res / 10;
            res = res % 10;

            ListNode* cur = new ListNode();
            cur->val = res;
            cur->next = new_head->next;
            new_head->next = cur;
        }

        return new_head->next;
    }
};