/*
 * @lc app=leetcode.cn id=206 lang=cpp
 *
 * [206] 反转链表
 */

// @lc code=start
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
    ListNode* reverseList(ListNode* head)
    {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }
        auto new_head = reverseList(head->next);

        head->next->next = head;
        head->next = nullptr;

        return new_head;
    }
};
// @lc code=end
