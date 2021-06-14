#include <vector>
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
    vector<int> ans;

    vector<int> reversePrint(ListNode* head)
    {
        reverse(head);
        return ans;
    }

    void reverse(ListNode* head)
    {
        if (head == nullptr) {
            return;
        }

        reverse(head->next);
        ans.push_back(head->val);
    }
};