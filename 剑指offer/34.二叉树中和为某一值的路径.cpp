#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode()
        : val(0)
        , left(nullptr)
        , right(nullptr)
    {
    }
    TreeNode(int x)
        : val(x)
        , left(nullptr)
        , right(nullptr)
    {
    }
    TreeNode(int x, TreeNode* left, TreeNode* right)
        : val(x)
        , left(left)
        , right(right)
    {
    }
};

class Solution {
public:
    vector<vector<int>> ans;
    int target = 0;

    void help(TreeNode* root, vector<int> path, int sum_)
    {
        path.push_back(root->val);
        sum_ += root->val;

        if (sum_ > target) {
            return;
        }

        if (sum_ == target && !root->left && !root->right) {
            ans.push_back(path);
            return;
        }

        if (root->left) {
            help(root->left, path, sum_);
        }
        if (root->right) {
            help(root->right, path, sum_);
        }
    }

    vector<vector<int>> pathSum(TreeNode* root, int target)
    {
        this->target = target;
        vector<int> path;
        if (!root) {
            return ans;
        }
        help(root, path, 0);
        return ans;
    }
};