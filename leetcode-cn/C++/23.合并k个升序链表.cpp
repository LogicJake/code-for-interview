/*
 * @lc app=leetcode.cn id=23 lang=cpp
 *
 * [23] 合并K个升序链表
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
    ListNode* mergeTwoList(ListNode* a, ListNode* b)
    {
        if (!a) {
            return b;
        }
        if (!b) {
            return a;
        }

        ListNode* ans = new ListNode(0);
        ListNode* cur = ans;

        while (a && b) {
            if (a->val <= b->val) {
                cur->next = a;
                a = a->next;
            } else {
                cur->next = b;
                b = b->next;
            }
            cur = cur->next;
        }
        if (a) {
            cur->next = a;
        } else {
            cur->next = b;
        }
        return ans->next;
    }

    ListNode* merge(vector<ListNode*>& lists, int left, int right)
    {
        if (left == right) {
            return lists[left];
        }
        if (left > right) {
            return nullptr;
        }
        int mid = (left + right) / 2;
        ListNode* merge_left = merge(lists, left, mid);
        ListNode* merge_right = merge(lists, mid + 1, right);
        return mergeTwoList(merge_left, merge_right);
    }

    ListNode* mergeKLists(vector<ListNode*>& lists)
    {
        return merge(lists, 0, lists.size() - 1);
    }
};
// @lc code=end
