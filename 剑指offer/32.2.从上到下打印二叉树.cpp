#include <deque>
#include <iostream>
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
    vector<vector<int>> levelOrder(TreeNode* root)
    {
        vector<vector<int>> ans;

        if (root == nullptr) {
            return ans;
        }

        deque<TreeNode*> queue;

        queue.push_back(root);

        while (not queue.empty()) {
            vector<int> tmp;

            int n = queue.size();
            for (int i = 0; i < n; i++) {
                TreeNode* cur = queue.front();
                queue.pop_front();

                tmp.push_back(cur->val);

                if (cur->left) {
                    queue.push_back(cur->left);
                }

                if (cur->right) {
                    queue.push_back(cur->right);
                }
            }

            ans.push_back(tmp);
        }

        return ans;
    }
};