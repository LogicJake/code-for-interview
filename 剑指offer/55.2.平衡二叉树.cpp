#include <iostream>
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
    bool ans = true;

    int help(TreeNode* root)
    {
        if (root == NULL || !ans) {
            return 0;
        }

        int left = help(root->right);
        int right = help(root->left);

        if (abs(left - right) > 1) {
            ans = false;
        }

        return max(left, right) + 1;
    }

    bool isBalanced(TreeNode* root)
    {
        help(root);
        return ans;
    }
};