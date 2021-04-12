/*
 * @lc app=leetcode.cn id=2 lang=cpp
 *
 * [2] 两数相加
 */

// @lc code=start
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
#include <iostream>
using namespace std;
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
    {
        ListNode* new_head = new ListNode();
        ListNode* cur = new_head;
        int carry = 0;

        while (l1 != nullptr or l2 != nullptr or carry != 0) {
            int a = 0;
            int b = 0;

            if (l1) {
                a = l1->val;
                l1 = l1->next;
            }
            if (l2) {
                b = l2->val;
                l2 = l2->next;
            }

            int res = a + b + carry;
            carry = res / 10;
            res = res % 10;

            ListNode* node = new ListNode(res);
            cur->next = node;
            cur = cur->next;
        }

        return new_head->next;
    }
};
// @lc code=end
