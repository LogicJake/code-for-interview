/*
 * @lc app=leetcode.cn id=25 lang=cpp
 *
 * [25] K 个一组翻转链表
 */

// @lc code=start
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode()
        : val(0)
        , next(nullptr)
    {
    }
    ListNode(int x)
        : val(x)
        , next(nullptr)
    {
    }
    ListNode(int x, ListNode* next)
        : val(x)
        , next(next)
    {
    }
};

class Solution {
public:
    pair<ListNode*, ListNode*> reverse(ListNode* head, ListNode* tail)
    {
        ListNode* pre = tail->next;
        ListNode* cur = head;
        while (pre != tail) {
            ListNode* next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }

        return { tail, head };
    }

    ListNode* reverseKGroup(ListNode* head, int k)
    {
        ListNode* new_head = new ListNode(0, head);

        ListNode* pre = new_head;
        ListNode* tail = pre;

        while (true) {
            for (int i = 0; i < k; i++) {
                tail = tail->next;
                if (!tail) {
                    return new_head->next;
                }
            }

            pair<ListNode*, ListNode*> res = reverse(head, tail);
            head = res.first;
            tail = res.second;

            pre->next = head;
            pre = tail;
            head = tail->next;
        }

        return new_head->next;
    }
};
// @lc code=end
