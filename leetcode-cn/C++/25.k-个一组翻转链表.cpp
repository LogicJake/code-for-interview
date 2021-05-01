/*
 * @lc app=leetcode.cn id=25 lang=cpp
 *
 * [25] K 个一组翻转链表
 */

// @lc code=start
#include <vector>
using namespace std;

// struct ListNode {
//     int val;
//     ListNode* next;
//     ListNode()
//         : val(0)
//         , next(nullptr)
//     {
//     }
//     ListNode(int x)
//         : val(x)
//         , next(nullptr)
//     {
//     }
//     ListNode(int x, ListNode* next)
//         : val(x)
//         , next(next)
//     {
//     }
// };

class Solution {
public:
    pair<ListNode*, ListNode*> reverse(ListNode* head, ListNode* tail)
    {
        ListNode* pre = tail->next;
        ListNode* p = head;
        while (pre != tail) {
            ListNode* next = p->next;
            p->next = pre;
            pre = p;
            p = next;
        }
        return { tail, head };
    }

    ListNode*
    reverseKGroup(ListNode* head, int k)
    {
        ListNode* new_head = new ListNode(0, head);
        ListNode* pre = new_head;
        ListNode* tail = pre;
        int num = 0;

        while (true) {
            for (int i = 0; i < k; i++) {
                tail = tail->next;
                // 不足k个提前退出
                if (!tail) {
                    return new_head->next;
                }
            }

            pair<ListNode*, ListNode*> result = reverse(head, tail);
            head = result.first;
            tail = result.second;

            pre->next = head;
            pre = tail;
            head = tail->next;
        }

        return new_head->next;
    }
};
// @lc code=end
