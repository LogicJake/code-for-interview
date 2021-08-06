/*
 * @lc app=leetcode.cn id=148 lang=cpp
 *
 * [148] 排序链表
 */

// @lc code=start
// struct ListNode
// {
//     int val;
//     ListNode *next;
//     ListNode() : val(0), next(nullptr) {}
//     ListNode(int x) : val(x), next(nullptr) {}
//     ListNode(int x, ListNode *next) : val(x), next(next) {}
// };

class Solution
{
public:
    ListNode *sortList(ListNode *head, ListNode *tail)
    {
        if (head == nullptr)
        {
            return head;
        }

        if (head->next == tail)
        {
            head->next = nullptr;
            return head;
        }

        ListNode *fast = head;
        ListNode *slow = head;

        while (fast != tail)
        {
            slow = slow->next;
            fast = fast->next;

            if (fast != tail)
            {
                fast = fast->next;
            }
        }

        ListNode *mid = slow;

        return merge(sortList(head, mid), sortList(mid, tail));
    }

    ListNode *merge(ListNode *p1, ListNode *p2)
    {
        ListNode *new_head = new ListNode(0);
        ListNode *cur = new_head;

        while (p1 != nullptr && p2 != nullptr)
        {
            if (p1->val < p2->val)
            {
                cur->next = p1;
                p1 = p1->next;
                cur = cur->next;
            }
            else
            {
                cur->next = p2;
                p2 = p2->next;
                cur = cur->next;
            }
        }

        if (p1)
        {
            cur->next = p1;
        }

        if (p2)
        {
            cur->next = p2;
        }
        return new_head->next;
    }

    ListNode *sortList(ListNode *head)
    {
        return sortList(head, nullptr);
    }
};
// @lc code=end
