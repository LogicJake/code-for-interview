#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x)
        : val(x)
        , left(NULL)
        , right(NULL)
    {
    }
};
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
    vector<ListNode*> listOfDepth(TreeNode* tree)
    {
        vector<ListNode*> ans;

        if (tree == nullptr) {
            return ans;
        }

        queue<TreeNode*> q;
        q.push(tree);

        while (!q.empty()) {
            int len = q.size();

            ListNode* head = new ListNode(0);
            ListNode* cur = head;
            for (int i = 0; i < len; i++) {
                TreeNode* node = q.front();
                q.pop();

                ListNode* new_node = new ListNode(node->val);
                cur->next = new_node;
                cur = cur->next;

                if (node->left) {
                    q.push(node->left);
                }
                if (node->right) {
                    q.push(node->right);
                }
            }

            ans.push_back(head->next);
        }

        return ans;
    }
};