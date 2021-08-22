/*
 * @lc app=leetcode.cn id=25 lang=cpp
 *
 * [25] K 个一组翻转链表
 */

// @lc code=start
#include <vector>
using namespace std;

// struct ListNode
// {
//     int val;
//     ListNode *next;
//     ListNode()
//         : val(0), next(nullptr)
//     {
//     }
//     ListNode(int x)
//         : val(x), next(nullptr)
//     {
//     }
//     ListNode(int x, ListNode *next)
//         : val(x), next(next)
//     {
//     }
// };

class Solution
{
public:
    pair<ListNode *, ListNode *> reverse(ListNode *head, ListNode *tail)
    {
        ListNode *pre = tail->next;
        ListNode *cur = head;

        while (pre != tail)
        {
            ListNode *next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }

        return {tail, head};
    }

    ListNode *reverseKGroup(ListNode *head, int k)
    {
        ListNode *new_head = new ListNode();
        new_head->next = head;

        ListNode *pre = new_head;
        ListNode *tail = new_head;

        while (1)
        {
            for (int i = 0; i < k; i++)
            {
                tail = tail->next;
                if (tail == nullptr)
                {
                    return new_head->next;
                }
            }

            pair<ListNode *, ListNode *> ret = reverse(head, tail);
            head = ret.first;
            tail = ret.second;

            pre->next = head;
            pre = tail;
            head = tail->next;
        }

        return new_head->next;
    }
};
// @lc code=end
