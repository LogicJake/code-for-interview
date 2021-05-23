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

class Solution {
public:
    vector<int> levelOrder(TreeNode* root)
    {
        vector<int> ans;
        queue<TreeNode*> q;
        if (!root) {
            return ans;
        }

        q.push(root);

        while (!q.empty()) {
            int sz = q.size();
            for (int i = 0; i < sz; i++) {
                auto cur = q.front();
                q.pop();

                ans.push_back(cur->val);

                if (cur->left) {
                    q.push(cur->left);
                }
                if (cur->right) {
                    q.push(cur->right);
                }
            }
        }
        return ans;
    }
};