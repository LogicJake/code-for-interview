#include <istream>
using namespace std;
struct ListNode {
    int val;
    struct ListNode* next;
    ListNode(int x)
        : val(x)
        , next(NULL)
    {
    }
};
class Solution {
public:
    ListNode* FindFirstCommonNode(ListNode* pHead1, ListNode* pHead2)
    {
        if (pHead1 == NULL or pHead2 == NULL) {
            return NULL;
        }

        ListNode* p = pHead1;
        ListNode* q = pHead2;

        while (p != q) {
            if (p == NULL) {
                p = pHead2;
            } else {
                p = p->next;
            }

            if (q == NULL) {
                q = pHead1;
            } else {
                q = q->next;
            }
        }

        return p;
    }
};