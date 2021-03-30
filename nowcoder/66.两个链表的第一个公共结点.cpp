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

        while (pHead1 != pHead2) {
            pHead1 = pHead1->next;
            pHead2 = pHead2->next;

            if (pHead1 == NULL) {
                /* code */
            }
        }
    }
};